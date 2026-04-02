import gradio as gr
import torch
import torch.nn as nn
from torchvision import models, transforms
import timm
from PIL import Image
import numpy as np
from pytorch_grad_cam import GradCAM
from pytorch_grad_cam.utils.image import show_cam_on_image

# =============================================================================
# 1. SETUP & CLASS NAMES
# =============================================================================
device = torch.device("cpu")

# Standard 38 PlantVillage Classes
CLASS_NAMES = [
    'Apple Scab', 'Apple Black rot', 'Apple Cedar rust', 'Apple healthy',
    'Blueberry healthy', 'Cherry Powdery mildew', 'Cherry healthy',
    'Corn Cercospora leaf spot', 'Corn Common rust', 'Corn Northern Leaf Blight', 'Corn healthy',
    'Grape Black rot', 'Grape Esca (Black Measles)', 'Grape Leaf blight', 'Grape healthy',
    'Orange Haunglongbing (Citrus greening)', 'Peach Bacterial spot', 'Peach healthy',
    'Pepper bell Bacterial spot', 'Pepper bell healthy', 'Potato Early blight', 'Potato Late blight', 'Potato healthy',
    'Raspberry healthy', 'Soybean healthy', 'Squash Powdery mildew', 'Strawberry Leaf scorch', 'Strawberry healthy',
    'Tomato Bacterial spot', 'Tomato Early blight', 'Tomato Late blight', 'Tomato Leaf Mold', 'Tomato Septoria leaf spot',
    'Tomato Spider mites', 'Tomato Target Spot', 'Tomato Yellow Leaf Curl Virus', 'Tomato mosaic virus', 'Tomato healthy'
]

FILE_NAMES = {
    "resnet": "ResNet18_final.pth",
    "effnet": "EfficientNet_final.pth",
    "vit": "vit_plant_model.pth"
}

def load_models():
    num_classes = len(CLASS_NAMES)
    
    # ResNet18
    m_res = models.resnet18(weights=None)
    m_res.fc = nn.Linear(m_res.fc.in_features, num_classes)
    m_res.load_state_dict(torch.load(FILE_NAMES["resnet"], map_location=device))
    m_res.eval()
    
    # EfficientNet (using non-strict for version compatibility)
    m_eff = models.efficientnet_b0(weights=None)
    m_eff.classifier[1] = nn.Linear(m_eff.classifier[1].in_features, num_classes)
    m_eff.load_state_dict(torch.load(FILE_NAMES["effnet"], map_location=device), strict=False)
    m_eff.eval()
    
    # ViT
    m_vit = timm.create_model('vit_base_patch16_224', pretrained=False, num_classes=num_classes)
    m_vit.load_state_dict(torch.load(FILE_NAMES["vit"], map_location=device))
    m_vit.eval()
    
    return m_res, m_eff, m_vit

try:
    model_res, model_eff, model_vit = load_models()
    LOAD_STATUS = "✅ System Ready"
except Exception as e:
    LOAD_STATUS = f"❌ Error: {e}"
    model_res = model_eff = model_vit = None

# =============================================================================
# 2. DIAGNOSTIC ENGINE
# =============================================================================
def reshape_transform(tensor, height=14, width=14):
    result = tensor[:, 1:, :].reshape(tensor.size(0), height, width, tensor.size(2))
    return result.transpose(2, 3).transpose(1, 2)

def run_diagnostic(img):
    if img is None: return "Please upload a leaf image.", None, None, None
    if model_res is None: return "Model not loaded.", None, None, None
    
    # Preprocess
    t = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    input_tensor = t(img).unsqueeze(0)
    rgb_img = np.array(img.resize((224, 224))) / 255.0

    # 1. PREDICTION (Using ResNet as the primary classifier)
    with torch.no_grad():
        output = model_res(input_tensor)
        prediction_idx = torch.argmax(output, dim=1).item()
        verdict = CLASS_NAMES[prediction_idx]
        
        # Simple Logic to check health
        health_status = "HEALTHY" if "healthy" in verdict.lower() else "DISEASED"
        final_output = f"Analysis: {verdict}\nStatus: {health_status}"

    # 2. GRAD-CAM (Explainable AI)
    with torch.enable_grad():
        # ResNet Map
        cam_res = GradCAM(model=model_res, target_layers=[model_res.layer4[-1]])
        res_viz = show_cam_on_image(rgb_img, cam_res(input_tensor=input_tensor)[0, :], use_rgb=True)
        
        # EffNet Map
        cam_eff = GradCAM(model=model_eff, target_layers=[model_eff.features[-1]])
        eff_viz = show_cam_on_image(rgb_img, cam_eff(input_tensor=input_tensor)[0, :], use_rgb=True)
        
        # ViT Map
        cam_vit = GradCAM(model=model_vit, target_layers=[model_vit.blocks[-1].norm1], reshape_transform=reshape_transform)
        vit_viz = show_cam_on_image(rgb_img, cam_vit(input_tensor=input_tensor)[0, :], use_rgb=True)

    return final_output, res_viz, eff_viz, vit_viz

# =============================================================================
# 3. UI
# =============================================================================
with gr.Blocks(theme=gr.themes.Monochrome()) as demo:
    gr.Markdown("# 🌿 Plant Path AI: Full Diagnostic Suite")
    gr.Markdown(f"**System Status:** {LOAD_STATUS}")
    
    with gr.Row():
        with gr.Column(scale=1):
            input_i = gr.Image(type="pil", label="Upload Leaf Specimen")
            btn = gr.Button("RUN FULL ANALYSIS", variant="primary")
            status = gr.Textbox(label="AI Verdict (Leaf Type & Disease)", lines=3)
        
        with gr.Column(scale=2):
            with gr.Row():
                o1 = gr.Image(label="ResNet18 Attention")
                o2 = gr.Image(label="EfficientNet Attention")
            o3 = gr.Image(label="ViT Global Attention")

    btn.click(run_diagnostic, input_i, [status, o1, o2, o3])

demo.launch()

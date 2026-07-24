<div align="center">

<!-- Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=soft&height=220&color=0:090A0F,50:0F172A,100:00F2FE&text=LOKATI%20RAGHUVARAN&fontSize=48&fontColor=F8FAFC&fontAlign=50&fontAlignY=42&animation=fadeIn&desc=Data%20Scientist%20%E2%80%A2%20Deep%20Learning%20Systems%20%E2%80%A2%20MLOps%20Engineer&descAlignY=62&descAlign=50" width="100%"/>

<br/>

<!-- Custom Typing SVG -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=3200&pause=1200&color=00F2FE&center=true&vCenter=true&width=800&lines=Building+Production-Grade+Multimodal+AI+Systems;Data+Science+%C2%B7+Deep+Learning+%C2%B7+MLOps;Architecting+scalable,+privacy-first+solutions;Quantizing+models+for+high-efficiency+edge+inference" />

<br/>

<!-- Premium Contact & Social Badges -->
<p align="center">
  <a href="mailto:raghuvaranlokati@gmail.com">
    <img src="https://img.shields.io/badge/Email-090A0F?style=for-the-badge&logo=gmail&logoColor=00F2FE" alt="Email" />
  </a>
  <a href="https://www.linkedin.com/in/lokati-raghuvaran-860572221/">
    <img src="https://img.shields.io/badge/LinkedIn-090F1C?style=for-the-badge&logo=linkedin&logoColor=0077B5" alt="LinkedIn" />
  </a>
  <a href="https://raghuvaran.vercel.app/">
    <img src="https://img.shields.io/badge/Portfolio-0D091F?style=for-the-badge&logo=vercel&logoColor=9B51E0" alt="Portfolio" />
  </a>
</p>

<sub>Based in India • Architecting the Future with Intelligence & Code</sub>

</div>

---

### 🧠 Core Philosophy & Engineering Focus
I design high-performance predictive systems, custom deep learning architectures, and scalable MLOps pipelines. I believe in **generalization over memorization**—building models that learn actual semantic meaning, handle edge-case noise, and maintain mathematical integrity under production traffic.

*   **Deep Learning Invariants:** Implementing rigorous neural sequence techniques (e.g., pre-padding for RNNs/LSTMs to preserve signals, SpatialDropout for regularizing CNNs).
*   **Multimodal Fusion:** Fusing unstructured signals (1D signals, 2D scans) with structured metadata.
*   **Edge Optimization:** Compiling and quantizing models (INT8/FP16) for low-power edge nodes.

---

### 🩺 Flagship Project: CardioGuard
> **Multimodal Clinical ECG & Heart Rhythm Analyzer**

CardioGuard is a production-grade deep learning framework that integrates 1D ECG lead sequential signals, 2D visual scans, and patient clinical metadata using a **Multimodal Fusion Network** to deliver state-of-the-art diagnostic accuracy, backed by explainable Grad-CAM heatmaps.

```mermaid
graph TD
    RawSignal["Raw 1D ECG Leads (12-Lead Voltages)"] --> SignalPrep["Bandpass Filter & Z-Score Normalization"]
    SignalPrep --> PrePadding["Pre-Padding (Start of Sequence)"]
    PrePadding --> LSTM["ECG1DNet (1D CNN + BiLSTM)"]
    
    RawImage["ECG Graph Image (Visual Scan)"] --> ImagePrep["Resize (128x128) & Standardize"]
    ImagePrep --> ResNet["ECG2DNet (2D ResNet/CNN)"]
    
    Metadata["Demographics (Age, Sex, History)"] --> MetaFC["Meta Projection Network (MLP)"]
    
    LSTM --> Concatenate["Multimodal Fusion Layer"]
    ResNet --> Concatenate
    MetaFC --> Concatenate
    
    Concatenate --> Classifier["Clinical Classifier (MLP + Softmax)"]
    Classifier --> Logits["Diagnostic Probabilities"]
    Logits --> XAI["Grad-CAM Localization Map"]
```

#### Key Architecture & MLOps Specs:
*   **ECG1DNet:** 1D Conv layers + BiLSTM utilizing **pre-padding sequence invariants** to prevent zero-padding from diluting the final hidden state classification signal.
*   **ECG2DNet:** Custom ResNet capturing anomalies from plotted visual scans, regularized using 2D Spatial Dropout (`0.3`).
*   **Explainability Gateway:** FastAPI backend that streams classification results paired with localized Grad-CAM anomaly intervals.

---

### 🚀 Highlighted Systems

#### 🛰️ ModelRoute-V2: Multi-Agent LLM Routing Engine
*   **Description:** An intelligent local router that classifies prompt complexity to dynamically direct queries. Low-complexity prompts run on local quantized models (Llama-3-8B), while high-complexity prompts route to commercial APIs, optimizing cloud resources.
*   **Results:** **64.2% API Cost Reduction** | **4.2ms Routing Latency** | **85M+ Tokens Optimized**
*   **Tech Stack:** `PyTorch`, `Transformers`, `FastAPI`, `Docker`, `Llama-3`, `BERT`

#### 🧬 DataSynth-LLM: Tabular Data Synthesizer
*   **Description:** A GAN-based pipeline combined with an LLM agent feedback loop that synthesizes realistic, HIPAA-compliant tabular medical datasets. The GAN models the distribution while the LLM acts as an expert validator checking clinical coherence.
*   **Results:** **98.7% Correlation Match** | **100.0% HIPAA Privacy Score** | **250 Epochs training cycles**
*   **Tech Stack:** `CTGAN`, `Python`, `Llama-3-Agent`, `Pandas`, `SciPy`, `W&B`

#### 👁️ VisionFlow: Edge Multi-Object Tracker
*   **Description:** A computer vision pipeline deploying YOLOv8 and ByteTrack on low-power devices. Optimized via post-training static quantization (INT8) to achieve high frame rates.
*   **Results:** **45.0 FPS on Raspberry Pi 4** | **91.2% MOTA Tracking Accuracy**
*   **Tech Stack:** `YOLOv8`, `OpenCV`, `TensorRT`, `C++`, `Docker`, `ONNX`

---

### 🛠️ Tech Stack & Arsenal

| Domain | Technologies |
| :--- | :--- |
| **Artificial Intelligence & DS** | `Python` `PyTorch` `TensorFlow` `Scikit-Learn` `Pandas` `NumPy` `Matplotlib` `Jupyter` |
| **Frontend & Mobile Dev** | `TypeScript` `JavaScript` `React` `Next.js` `TailwindCSS` `Expo` `Redux` `HTML/CSS` |
| **Backend & Cloud** | `Node.js` `Express` `MongoDB` `Firebase` `Supabase` `FastAPI` `PostgreSQL` |
| **DevOps & Tooling** | `Git` `GitHub` `Docker` `Linux` `AWS` `Vercel` `Weights & Biases (W&B)` |

---

### 📈 GitHub Analytics & Status

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=Raghuvaranlokati&show_icons=true&bg_color=090A0F&title_color=00F2FE&text_color=F8FAFC&icon_color=9B51E0&border_color=1E293B&hide_border=false" width="48%" />
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=Raghuvaranlokati&theme=tokyonight&border_radius=8&hide_border=true" width="48%" />
  <br/><br/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Raghuvaranlokati&layout=compact&bg_color=090A0F&title_color=00F2FE&text_color=F8FAFC&icon_color=9B51E0&border_color=1E293B&hide_border=false" width="48%" />
  <img src="https://github.com/Raghuvaranlokati/Raghuvaranlokati/blob/output/github-contribution-grid-snake.svg" alt="Contribution Snake" width="48%" />
</div>

<br/>

<div align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=Raghuvaranlokati&bg_color=090A0F&color=00F2FE&line=9B51E0&point=00F2FE&area=true&hide_border=true" alt="Activity Graph" width="100%" />
</div>

---

<div align="center">

### 💡 Developer Quote
<img src="https://quotes-github-readme.vercel.app/api?type=horizontal&theme=tokyonight" alt="Quote" />

<br/>

### ☕ Fuel the Journey
If you like my systems or open-source research, consider supporting my coding sprints!
<br/><br/>
<a href="https://www.buymeacoffee.com/raghuvaranl">
  <img src="https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me A Coffee" />
</a>
<a href="https://ko-fi.com/raghuvaran">
  <img src="https://img.shields.io/badge/Ko--fi-FF5E5B?style=for-the-badge&logo=ko-fi&logoColor=white" alt="Ko-fi" />
</a>

</div>

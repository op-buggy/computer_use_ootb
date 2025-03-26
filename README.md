<h2 align="center">
    <a href="https://computer-use-ootb.github.io">
        <img src="./assets/ootb_logo.png" alt="Logo" style="display: block; margin: 0 auto; filter: invert(1) brightness(2);">
    </a>
</h2>

<h5 align="center">如果您喜欢我们的项目，请在GitHub上给我们一个⭐星标以获取最新更新。</h5>

<h5 align=center>

[![arXiv](https://img.shields.io/badge/Arxiv-2411.10323-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2411.10323)
[![Project Page](https://img.shields.io/badge/Project_Page-GUI_Agent-blue)](https://computer-use-ootb.github.io)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fshowlab%2Fcomputer_use_ootb&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fshowlab%2Fcomputer_use_ootb&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)

</h5>

## <img src="./assets/ootb_icon.png" alt="Star" style="height:25px; vertical-align:middle; filter: invert(1) brightness(2);"> 概述
**Computer Use <span style="color:rgb(106, 158, 210)">O</span><span style="color:rgb(111, 163, 82)">O</span><span style="color:rgb(209, 100, 94)">T</span><span style="color:rgb(238, 171, 106)">B</span>**<img src="./assets/ootb_icon.png" alt="Star" style="height:20px; vertical-align:middle; filter: invert(1) brightness(2);"> 是一个开箱即用（OOTB）的桌面GUI代理解决方案，包括基于API的（**Claude 3.5 Computer Use**）和本地运行模型（**<span style="color:rgb(106, 158, 210)">S</span><span style="color:rgb(111, 163, 82)">h</span><span style="color:rgb(209, 100, 94)">o</span><span style="color:rgb(238, 171, 106)">w</span>UI**、**UI-TARS**）。

**无需Docker**，同时支持**Windows**和**macOS**。OOTB提供了一个基于Gradio的用户友好界面。🎨

访问我们关于Claude 3.5 Computer Use的GUI代理研究[[项目页面]](https://computer-use-ootb.github.io)。🌐

## 更新日志
- **[2025/02/08]** 我们添加了对[**UI-TARS**](https://github.com/bytedance/UI-TARS)的支持。按照[云部署](https://github.com/bytedance/UI-TARS?tab=readme-ov-file#cloud-deployment)或[VLLM部署](https://github.com/bytedance/UI-TARS?tab=readme-ov-file#local-deployment-vllm)指南在OOTB中本地实现UI-TARS。
- **重大更新！[2024/12/04]** **本地运行🔥**现已上线！向[**<span style="color:rgb(106, 158, 210)">S</span><span style="color:rgb(111, 163, 82)">h</span><span style="color:rgb(209, 100, 94)">o</span><span style="color:rgb(238, 171, 106)">w</span>UI**](https://github.com/showlab/ShowUI)问好，这是一个开源的2B视觉-语言-动作（VLA）模型，用于GUI代理。现在兼容`"gpt-4o + ShowUI"（约便宜200倍）`*和`"Qwen2-VL + ShowUI"（约便宜30倍）`*，每个任务只需几美分💰！<span style="color: grey; font-size: small;">*相比Claude Computer Use</span>。
- **[2024/11/20]** 我们添加了一些示例，帮助您获得Claude 3.5 Computer Use的实践经验。
- **[2024/11/19]** 忘记Anthropic设置的单显示器限制 - 您现在可以使用**多显示器** 🎉！
- **[2024/11/18]** 我们发布了Claude 3.5 Computer Use的深入分析：[https://arxiv.org/abs/2411.10323](https://arxiv.org/abs/2411.10323)。
- **[2024/11/11]** 忘记Anthropic设置的低分辨率显示限制 - 您现在可以使用*任何分辨率*，同时保持**截图token成本低** 🎉！
- **[2024/11/11]** 现在同时支持**Windows**和**macOS**平台 🎉！
- **[2024/10/25]** 现在您可以通过移动设备📱**远程控制**您的电脑💻 - **无需安装移动应用**！试试看，玩得开心 🎉。

## 演示视频

https://github.com/user-attachments/assets/f50b7611-2350-4712-af9e-3d31e30020ee

<div style="display: flex; justify-content: space-around;">
  <a href="https://youtu.be/Ychd-t24HZw" target="_blank" style="margin-right: 10px;">
    <img src="https://img.youtube.com/vi/Ychd-t24HZw/maxresdefault.jpg" alt="观看视频" width="48%">
  </a>
  <a href="https://youtu.be/cvgPBazxLFM" target="_blank">
    <img src="https://img.youtube.com/vi/cvgPBazxLFM/maxresdefault.jpg" alt="观看视频" width="48%">
  </a>
</div>

## 🚀 快速开始

### 0. 前置条件
- 通过此[链接](https://www.anaconda.com/download?utm_source=anacondadocs&utm_medium=documentation&utm_campaign=download&utm_content=topnavalldocs)在您的系统上安装Miniconda。（**Python版本：>= 3.12**）。
- 硬件要求（可选，用于ShowUI本地运行）：
    - **Windows（支持CUDA）：** 兼容的NVIDIA GPU，支持CUDA，>=6GB显存
    - **macOS（Apple Silicon）：** M1芯片（或更新），>=16GB统一内存

### 1. 克隆仓库 📂
打开Conda终端。（安装Miniconda后，它会在开始菜单中出现。）
在**Conda终端**中运行以下命令。
```bash
git clone https://github.com/showlab/computer_use_ootb.git
cd computer_use_ootb
```

### 2.1 安装依赖 🔧
```bash
pip install -r requirements.txt
```

### 2.2 （可选）为**<span style="color:rgb(106, 158, 210)">S</span><span style="color:rgb(111, 163, 82)">h</span><span style="color:rgb(209, 100, 94)">o</span><span style="color:rgb(238, 171, 106)">w</span>UI**本地运行做准备

1. 通过以下命令下载ShowUI-2B模型的所有文件。确保`ShowUI-2B`文件夹位于`computer_use_ootb`文件夹下。

    ```python
    python install_tools/install_showui.py
    ```

2. 确保在您的机器上安装正确GPU版本的PyTorch（CUDA、MPS等）。参见[安装指南和验证](https://pytorch.org/get-started/locally/)。

3. 获取[GPT-4o](https://platform.openai.com/docs/quickstart)或[Qwen-VL](https://help.aliyun.com/zh/dashscope/developer-reference/acquisition-and-configuration-of-api-key)的API密钥。中国大陆用户可获得Qwen API的100万token免费试用[链接](https://help.aliyun.com/zh/dashscope/developer-reference/tongyi-qianwen-vl-plus-api)。

### 2.3 （可选）为**UI-TARS**本地运行做准备

1. 按照[云部署](https://github.com/bytedance/UI-TARS?tab=readme-ov-file#cloud-deployment)或[VLLM部署](https://github.com/bytedance/UI-TARS?tab=readme-ov-file#local-deployment-vllm)指南部署您的UI-TARS服务器。

2. 使用脚本`.\install_tools\test_ui-tars_server.py`测试您的UI-TARS服务器。

### 2.4 （可选）如果您想在ssh服务器上部署Qwen模型作为规划器
1. 在您的ssh服务器上克隆此项目

2. python computer_use_demo/remote_inference.py

### 3. 启动界面 ▶️

**启动OOTB界面：**
```bash
python app.py
```
如果您成功启动界面，您将在终端中看到两个URL：
```bash
* Running on local URL:  http://127.0.0.1:7860
* Running on public URL: https://xxxxxxxxxxxxxxxx.gradio.live（不要与他人分享此链接，否则他们将能够控制您的计算机。）
```

> <u>为方便起见</u>，我们建议在启动界面之前运行以下一个或多个命令来设置API密钥到环境变量。这样您就不需要在每次运行时手动传递密钥。在Windows PowerShell上（如果在cmd上使用`set`命令）：
> ```bash
> $env:ANTHROPIC_API_KEY="sk-xxxxx"（替换为您自己的密钥）
> $env:QWEN_API_KEY="sk-xxxxx"
> $env:OPENAI_API_KEY="sk-xxxxx"
> ```
> 在macOS/Linux上，将上述命令中的`$env:ANTHROPIC_API_KEY`替换为`export ANTHROPIC_API_KEY`。

### 4. 使用任何可访问互联网的设备控制您的计算机
- **被控制的计算机**：安装了软件的计算机。
- **发送命令的设备**：打开网站的设备。
  
在您的移动浏览器中打开http://localhost:7860/（如果您正在控制同一台计算机）或https://xxxxxxxxxxxxxxxxx.gradio.live进行远程控制。

输入Anthropic API密钥（您可以通过此[网站](https://console.anthropic.com/settings/keys)获取），然后给出命令让AI执行您的任务。

### ShowUI高级设置

我们提供4位量化版本的ShowUI-2B模型用于成本效益推理（目前**仅支持CUDA设备**）。要下载4位量化版本的ShowUI-2B模型：
```
python install_tools/install_showui-awq-4bit.py
```
然后，在'ShowUI高级设置'下拉菜单中启用量化设置。

此外，我们还提供了一个滑块来快速调整ShowUI模型中的`max_pixel`参数。这控制模型的视觉输入大小，并极大地影响内存和推理速度。

## 📊 GUI代理模型库

现在，OOTB支持通过以下模型自定义GUI代理：

- **统一模型**：统一的规划器和执行器，可以同时进行高级规划和低级控制。
- **规划器**：通用LLM，用于处理高级规划和决策。
- **执行器**：视觉-语言-动作模型，用于处理低级控制和动作命令生成。

<div align="center">
  <b>OOTB支持的GUI代理模型</b>
</div>
<table align="center">
  <tbody>
    <tr align="center" valign="bottom">
      <td>
        <b>[API] 统一模型</b>
      </td>
      <td>
        <b>[API] 规划器</b>
      </td>
      <td>
        <b>[本地] 规划器</b>
      </td>
      <td>
        <b>[API] 执行器</b>
      </td>
      <td>
        <b>[本地] 执行器</b>
      </td>
    </tr>
    <tr valign="top">
      <td>
        <ul>
            <li><a href="">Claude 3.5 Sonnet</a></li>
      </ul>
      </td>
      <td>
        <ul>
          <li><a href="">GPT-4o</a></li>
          <li><a href="">Qwen2-VL-Max</a></li>
          <li><a href="">Qwen2-VL-2B(ssh)</a></li>
          <li><a href="">Qwen2-VL-7B(ssh)</a></li>
          <li><a href="">Qwen2.5-VL-7B(ssh)</a></li>
          <li><a href="">Deepseek V3（即将推出）</a></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="">Qwen2-VL-2B</a></li>
          <li><a href="">Qwen2-VL-7B</a></li>
        </ul>
      </td>
        <td>
        <ul>
          <li><a href="https://github.com/showlab/ShowUI">ShowUI</a></li>
          <li><a href="https://huggingface.co/bytedance-research/UI-TARS-7B-DPO">UI-TARS-7B/72B-DPO（即将推出）</a></li> 
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="https://github.com/showlab/ShowUI">ShowUI</a></li>
          <li><a href="https://huggingface.co/bytedance-research/UI-TARS-7B-DPO">UI-TARS-7B/72B-DPO</a></li>
        </ul>
      </td>
    </tr>
</td>
</table>

> 其中[API]模型基于远程推理的LLM API调用，
而[本地]模型可以在您自己的设备上本地推理，无需API费用。

## 🖥️ 支持的系统
- **Windows**（Claude ✅, ShowUI ✅）
- **macOS**（Claude ✅, ShowUI ✅）

## 👓 OOTB界面
<div style="display: flex; align-items: center; gap: 10px;">
  <figure style="text-align: center;">
    <img src="./assets/gradio_interface.png" alt="桌面界面" style="width: auto; object-fit: contain;">
  </figure>
</div>

## ⚠️ 风险提示
- **模型可能执行危险操作**：模型的性能仍然有限，可能产生意外或潜在有害的输出。建议持续监控AI的操作。
- **成本控制**：每个任务使用Claude 3.5 Computer Use可能需要几美元。💸

## 📅 路线图
- [ ] **探索可用功能**
  - [ ] Claude API在解决任务时似乎不稳定。我们正在调查原因：分辨率、所需操作类型、操作系统平台或规划机制。欢迎任何想法或评论。
- [ ] **界面设计**
  - [x] **支持Gradio** ✨
  - [ ] **更简单的安装**
  - [ ] **更多功能**... 🚀
- [ ] **平台**
  - [x] **Windows**
  - [x] **macOS**
  - [x] **移动设备**（发送命令）
  - [ ] **移动设备**（被控制）
- [ ] **支持更多MLLM**
  - [x] **Claude 3.5 Sonnet** 🎵
  - [x] **GPT-4o**
  - [x] **Qwen2-VL**
  - [ ] **本地MLLM**
  - [ ] ...
- [ ] **改进提示策略**
  - [ ] 优化提示以提高成本效益。💡
- [x] **改进推理速度**
  - [x] 支持int4量化。

## 加入讨论
欢迎与我们讨论并持续改进Computer Use - OOTB的用户体验。通过这个[**Discord频道**](https://discord.gg/vMMJTSew37)或下面的微信二维码联系我们！

<div style="display: flex; flex-direction: row; justify-content: space-around;">
<img src="./assets/wechat_3.jpg" alt="gradio_interface" width="30%">
</div>

<div style="height: 30px;"></div>

<hr>
<a href="https://computer-use-ootb.github.io">
<img src="./assets/ootb_logo.png" alt="Logo" width="30%" style="display: block; margin: 0 auto; filter: invert(1) brightness(2);">
</a> 
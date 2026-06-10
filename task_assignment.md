# DP-fy Your DATA - Task Assignment (7 Members)

## Overview

Video chủ đề:

> **DP-fy your DATA: How to (and why) synthesize Differentially Private Synthetic Data**

Mỗi thành viên phụ trách nghiên cứu lý thuyết, thiết kế animation/slides và triển khai một scene tương ứng.

---

## Task Assignment

| Người | Chủ đề                               | Nội dung cần nghiên cứu                                                                                                                                         | Nội dung trực quan / Animation                                                                                                                                                                                                                     | File                               |
| ----- | ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| **1** | **Data in Machine Learning**         | - Vai trò của dữ liệu trong AI/ML<br>- Các loại dữ liệu: Text, Image, Tabular<br>- Dữ liệu là "nhiên liệu" của AI<br>- Các vấn đề riêng tư khi thu thập dữ liệu | - Data → Model → Prediction<br>- Hiện các nguồn dữ liệu (Medical Records, User Profiles, Financial Data)<br>- Dữ liệu đổ vào mô hình AI<br>- Xuất hiện cảnh báo Privacy Risk<br>- Kết thúc bằng câu hỏi: *Can we use data without exposing users?* | `scene1_data_ml.py`                |
| **2** | **Differential Privacy**             | - Differential Privacy là gì<br>- Neighboring Datasets<br>- ε-DP<br>- Privacy Guarantee<br>- Laplace & Gaussian Mechanism<br>- Privacy Budget                   | - Hai database D₁ và D₂ khác nhau 1 người<br>- Cùng chạy qua một thuật toán<br>- Hai phân phối xác suất gần như giống nhau<br>- Minh họa thêm nhiễu vào kết quả truy vấn<br>- Highlight: *One person's data should not matter*                     | `scene2_differential_privacy.py`   |
| **3** | **DP Synthetic Text**                | - Privacy trong NLP<br>- LLM Memorization<br>- DP-SGD<br>- Fine-tuning với DP<br>- Private Evolution                                                            | - Hiển thị dữ liệu nhạy cảm: "John has cancer"<br>- Transformer Architecture<br>- Gradient Clipping<br>- Noise Injection<br>- Sinh văn bản tổng hợp<br>- So sánh Real Text vs Synthetic Text                                                       | `scene3_dp_text.py`                |
| **4** | **DP Synthetic Images**              | - Image Privacy Risks<br>- DP-GAN<br>- DP Diffusion Models<br>- Memorization trong Vision Models                                                                | - Real Images → DP Training → Synthetic Images<br>- Minh họa ảnh MNIST hoặc khuôn mặt<br>- So sánh ảnh thật và ảnh tổng hợp<br>- Hiệu ứng nhiễu trên pixel                                                                                         | `scene4_dp_images.py`              |
| **5** | **DP Synthetic Tabular Data**        | - Tabular Data<br>- Healthcare & Census Data<br>- Bayesian Networks<br>- PrivBayes<br>- Correlation Preservation                                                | - Bảng dữ liệu Age, Income, Disease<br>- Chuyển sang Bayesian Network<br>- Hiển thị quan hệ giữa các thuộc tính<br>- Sinh Synthetic Table mới<br>- So sánh dữ liệu thật và dữ liệu tổng hợp                                                        | `scene5_dp_tabular.py`             |
| **6** | **Important Privacy Considerations** | - Utility vs Privacy Trade-off<br>- Membership Inference Attack<br>- Re-identification Risk<br>- Privacy Auditing<br>- Evaluation Metrics                       | - Thanh cân bằng Privacy ↔ Utility<br>- Kẻ tấn công cố xác định một record có trong dữ liệu huấn luyện hay không<br>- Biểu đồ Utility / Privacy / Fidelity<br>- Minh họa trade-off giữa chất lượng và bảo mật                                      | `scene6_privacy_considerations.py` |
| **7** | **Conclusion & Complete System**     | - Tổng hợp toàn bộ tutorial<br>- Khi nào nên dùng DP Synthetic Data<br>- Ưu điểm và hạn chế<br>- Ứng dụng thực tế                                               | - Pipeline hoàn chỉnh:<br>Raw Data → DP → Synthetic Data → Evaluation → Publish<br>- Sơ đồ tổng hợp các phần trước<br>- Kết thúc với thông điệp: *Protect Privacy, Unlock Data*                                                                    | `scene7_conclusion.py`             |

---

## Estimated Duration

| Người | Thời lượng   |
| ----- | ------------ |
| 1     | 1.5 – 2 phút |
| 2     | 2 – 3 phút   |
| 3     | 2 – 3 phút   |
| 4     | 2 phút       |
| 5     | 2 phút       |
| 6     | 2 phút       |
| 7     | 1.5 – 2 phút |

**Tổng thời lượng video dự kiến:** 14–16 phút.

# Đồng bộ

## Link: https://slideslive.com/icml-2025/dpfy-your-data-how-to-and-why-synthesize-differentially-private-synthetic-data?utm_source=chatgpt.com (Link cũ bị lỗi).

## Link giọng AI: https://www.everai.vn/text-to-speech (chọn giọng Minh Quân)

## Đồng bộ Thị giác

**Màu nền:** Đen tuyền

**Font chữ:** Arial

**Công thức:** Công thức toán bắt buộc gõ bằng LaTeX(màu trắng).
import os
from manim import *
import numpy as np

class Scene3DPText(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # ========== AUDIO ==========
        audio_path = "assets\\audio\\scene3_dp_text.mp3"
        if os.path.exists(audio_path):
            self.add_sound(audio_path)
        else:
            print(f"Warning: audio not found at {audio_path}")

        # ========== TIMELINE HELPERS ==========
        clock = {"t": 0.0}

        def play_sync(*animations, run_time=1.0, **kwargs):
            self.play(*animations, run_time=run_time, **kwargs)
            clock["t"] += run_time

        def wait_until(target_time):
            gap = target_time - clock["t"]
            if gap > 0:
                self.wait(gap)
                clock["t"] = target_time

        # ========== STYLE HELPERS ==========
        FONT = "Arial"
        def txt(text, scale=0.5, color=WHITE, weight="NORMAL", line_spacing=-1):
            t = Text(text, font=FONT, color=color, weight=weight)
            if line_spacing > 0:
                t.line_spacing = line_spacing
            return t.scale(scale)

        # ========== CÁC MỐC THỜI GIAN (từ SRT, có hiệu chỉnh nhẹ) ==========
        T_END_INTRO = 8.5
        T_END_LLM_INTRO = 13.1
        T_END_RISK = 21.839
        T_END_QUESTION = 31.0
        T_END_DP_SGD_INTRO = 37.0
        T_END_TWO_STEPS = 52.0
        T_END_CLIP_EXPLAIN = 63.364
        T_END_NOISE_EXPLAIN = 72.923
        T_END_FORMULA = 84.472
        T_END_PARAMS = 90.568
        T_END_GUARANTEE = 94.614
        T_END_DRAWBACK = 100.0
        T_END_PE_INTRO = 108.807
        T_END_PE_MECH = 114.429
        T_END_PE_LOOP = 122.0
        T_END_AUGPE = 132.75
        T_END_AUGPE_STRENGTH = 142.386
        T_END_RESULT_INTRO = 143.0
        T_END_COMPARE = 161.061      # Kết thúc so sánh
        T_END_CONCLUSION = 168.302    # Bắt đầu câu kết luận
        T_END_FINAL = 173.831

        # ========== PHẦN 1: MỞ ĐẦU ==========
        title = txt("DP Synthetic Text", scale=0.70, weight="BOLD")
        title.to_edge(UP)
        play_sync(Write(title), run_time=1.2)
        wait_until(T_END_INTRO)

        # ========== LLM + MEMORIZATION + VÍ DỤ ==========
        llm_box = Rectangle(height=2, width=3, color=BLUE, fill_opacity=0.2)
        llm_label = txt("LLM", scale=0.55, color=BLUE).move_to(llm_box)
        play_sync(Create(llm_box), Write(llm_label), run_time=1.0)
        wait_until(T_END_LLM_INTRO)

        risk_text = txt("PRIVACY RISK: Memorization!", scale=0.55, color=RED)
        risk_text.next_to(llm_box, DOWN, buff=0.5)
        play_sync(Write(risk_text), run_time=1.0)
        wait_until(T_END_RISK)

        sensitive = txt("John has cancer", scale=0.65, color=RED)
        sensitive.move_to(UP*2.5)
        arrow = Arrow(sensitive.get_bottom(), llm_box.get_top(), color=WHITE)
        play_sync(FadeIn(sensitive, shift=DOWN), GrowArrow(arrow), run_time=1.0)
        wait_until(T_END_QUESTION)

        question = txt("How to use data without exposing users?", scale=0.55, color=YELLOW)
        question.next_to(risk_text, DOWN, buff=0.6)
        play_sync(Write(question), run_time=1.2)
        wait_until(T_END_QUESTION)

        play_sync(FadeOut(title), FadeOut(sensitive), FadeOut(llm_box), FadeOut(llm_label),
                  FadeOut(arrow), FadeOut(risk_text), FadeOut(question), run_time=1.0)
        wait_until(T_END_DP_SGD_INTRO - 0.5)

        # ========== PHẦN 2: DP-SGD ==========
        sgd_title = txt("Solution 1: DP-SGD Fine-tuning", scale=0.65, weight="BOLD")
        sgd_title.to_edge(UP)
        play_sync(Write(sgd_title), run_time=1.0)
        wait_until(T_END_DP_SGD_INTRO)

        step1 = txt("Step 1: Gradient Clipping", scale=0.45, color=YELLOW)
        step2 = txt("Step 2: Noise Injection", scale=0.45, color=YELLOW)
        steps = VGroup(step1, step2).arrange(DOWN, buff=0.4).next_to(sgd_title, DOWN, buff=0.5)
        play_sync(Write(steps), run_time=1.2)
        wait_until(T_END_TWO_STEPS)
        play_sync(FadeOut(steps), run_time=0.5)

        # ---- Gradient Clipping ----
        clip_title = txt("Step 1: Gradient Clipping", scale=0.55, color=YELLOW)
        clip_title.next_to(sgd_title, DOWN, buff=0.3)
        play_sync(Write(clip_title), run_time=0.8)

        gradients = VGroup(
            Arrow(LEFT, RIGHT*1.5, color=BLUE, stroke_width=6),
            Arrow(LEFT, RIGHT*3.0, color=YELLOW, stroke_width=6),
            Arrow(LEFT, RIGHT*5.0, color=RED, stroke_width=6),
        ).arrange(DOWN, buff=0.8).move_to(ORIGIN)
        play_sync(Create(gradients), run_time=1.2)

        threshold = DashedLine(start=LEFT*3.2 + UP*1.0, end=RIGHT*3.2 + UP*1.0, color=WHITE)
        th_label = txt("C", scale=0.4).next_to(threshold, RIGHT)
        play_sync(Create(threshold), Write(th_label), run_time=0.8)

        clipped = Transform(gradients[2], Arrow(LEFT, RIGHT*3.0, color=RED, stroke_width=8))
        clip_mark = txt("Clip!", scale=0.45, color=RED).move_to(gradients[2].get_center())
        play_sync(clipped, Write(clip_mark), run_time=1.0)
        play_sync(FadeOut(clip_title), FadeOut(gradients), FadeOut(threshold), FadeOut(th_label), FadeOut(clip_mark), run_time=0.5)
        wait_until(T_END_CLIP_EXPLAIN)

        # ---- Noise Injection ----
        noise_title = txt("Step 2: Noise Injection", scale=0.55, color=YELLOW)
        noise_title.next_to(sgd_title, DOWN, buff=0.3)
        play_sync(Write(noise_title), run_time=0.8)

        total_grad = Arrow(LEFT, RIGHT*3.0, color=GREEN, stroke_width=8)
        total_label = txt("Aggregated Gradient", scale=0.4, color=GREEN).next_to(total_grad, DOWN)
        play_sync(Create(total_grad), Write(total_label), run_time=1.0)

        center = total_grad.get_center()
        noise_dots = VGroup(*[
            Dot(radius=0.05, color=WHITE).move_to(
                center + np.array([np.random.uniform(-1.5, 1.5), np.random.uniform(-1.5, 1.5), 0])
            ) for _ in range(80)
        ])
        noise_effect = txt("+ Gaussian Noise", scale=0.4).next_to(noise_dots, RIGHT)
        play_sync(Create(noise_dots), Write(noise_effect), run_time=1.0)
        noisy_grad = total_grad.copy().set_color(ORANGE)
        play_sync(Transform(total_grad, noisy_grad), run_time=0.8)
        play_sync(FadeOut(noise_title), FadeOut(total_grad), FadeOut(total_label), FadeOut(noise_dots), FadeOut(noise_effect), run_time=0.5)
        wait_until(T_END_NOISE_EXPLAIN)

        # ---- Công thức ----
        formula = MathTex(
            r"\tilde{g} = \frac{1}{B}\left[\sum \text{clip}(g_i, C) + \mathcal{N}(0, \sigma^2 C^2)\right]",
            color=WHITE
        ).scale(0.7).to_edge(DOWN)
        play_sync(Write(formula), run_time=1.2)
        wait_until(T_END_FORMULA)

        params = txt("g_i: gradient of sample i, B: batch size, σ: noise factor", scale=0.35, color=GRAY)
        params.next_to(formula, UP, buff=0.2)
        play_sync(Write(params), run_time=1.0)
        wait_until(T_END_PARAMS)

        play_sync(FadeOut(formula), FadeOut(params), run_time=0.5)
        wait_until(T_END_GUARANTEE)

        guarantee = txt("Changing any single data sample\nhas almost no effect on the output.", scale=0.5, line_spacing=0.5)
        guarantee.move_to(ORIGIN)
        play_sync(Write(guarantee), run_time=1.0)
        wait_until(T_END_GUARANTEE)
        play_sync(FadeOut(guarantee), run_time=0.5)
        wait_until(T_END_DRAWBACK)

        drawback = txt("However, DP-SGD requires deep model access\nand heavy computational resources.", scale=0.5, color=RED, line_spacing=0.5)
        drawback.move_to(ORIGIN)
        play_sync(Write(drawback), run_time=1.0)
        wait_until(T_END_DRAWBACK)
        play_sync(FadeOut(drawback), FadeOut(sgd_title), run_time=0.5)
        wait_until(T_END_PE_INTRO - 3.0)

        # ========== PHẦN 3: PE & Aug-PE ==========
        pe_title = txt("Solution 2: Private Evolution (PE)", scale=0.65, weight="BOLD")
        pe_title.to_edge(UP)
        play_sync(Write(pe_title), run_time=1.5)
        wait_until(T_END_PE_INTRO)

        priv_data = txt("Private Data", scale=0.45, color=RED).shift(LEFT*3.5)
        api = Rectangle(height=2, width=4, color=PURPLE, fill_opacity=0.2).shift(RIGHT)
        api_label = txt("LLM API", scale=0.45, color=PURPLE).move_to(api)
        arrow1 = Arrow(priv_data.get_right(), api.get_left(), color=WHITE)
        synth = txt("Synthetic Text", scale=0.45, color=GREEN).shift(RIGHT*5)
        arrow2 = Arrow(api.get_right(), synth.get_left(), color=WHITE)
        play_sync(FadeIn(priv_data, shift=UP), Create(api), Write(api_label), GrowArrow(arrow1), run_time=1.2)
        play_sync(FadeIn(synth, shift=UP), GrowArrow(arrow2), run_time=1.0)
        wait_until(T_END_PE_MECH)

        loop = txt("Iterate: Generate → Score → Select", scale=0.4, color=YELLOW).next_to(api, DOWN, buff=0.6)
        play_sync(Write(loop), run_time=1.0)
        wait_until(T_END_PE_LOOP)

        play_sync(FadeOut(pe_title), FadeOut(priv_data), FadeOut(api), FadeOut(api_label),
                  FadeOut(arrow1), FadeOut(synth), FadeOut(arrow2), FadeOut(loop), run_time=0.8)
        wait_until(T_END_AUGPE - 0.5)

        aug_title = txt("Augmented Private Evolution (Aug-PE)", scale=0.65, weight="BOLD")
        aug_title.to_edge(UP)
        play_sync(Write(aug_title), run_time=1.0)
        wait_until(T_END_AUGPE)

        aug_box = Rectangle(height=2, width=5, color=GREEN, fill_opacity=0.2).move_to(ORIGIN)
        aug_label = txt("Aug-PE", scale=0.55, color=GREEN).move_to(aug_box)
        play_sync(Create(aug_box), Write(aug_label), run_time=1.0)

        strengths = VGroup(
            txt("✓ No model training", scale=0.4, color=GREEN),
            txt("✓ Only API access", scale=0.4, color=GREEN),
            txt("✓ Works with closed-source models", scale=0.4, color=GREEN),
            txt("✓ Competitive with DP-SGD for text", scale=0.4, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(aug_box, DOWN, buff=0.5)
        play_sync(Write(strengths), run_time=1.5)
        wait_until(T_END_AUGPE_STRENGTH)

        play_sync(FadeOut(aug_title), FadeOut(aug_box), FadeOut(aug_label), FadeOut(strengths), run_time=0.8)
        wait_until(T_END_RESULT_INTRO - 0.5)

        # ========== PHẦN 4: KẾT QUẢ ==========
        result_title = txt("Result: Real vs Synthetic Text", scale=0.65, weight="BOLD")
        result_title.to_edge(UP)
        play_sync(Write(result_title), run_time=1.0)
        wait_until(T_END_RESULT_INTRO)

        real_box = Rectangle(height=3.5, width=5.5, color=RED, fill_opacity=0.15, stroke_width=4).shift(LEFT*3.5)
        real_title = txt("Real Text", scale=0.55, color=RED).move_to(real_box.get_top()+UP*0.3)
        real_content = txt("John has cancer.\nHis medical history\nincludes chemotherapy\nand radiation.", scale=0.4, color=RED, line_spacing=0.5).move_to(real_box)

        syn_box = Rectangle(height=3.5, width=5.5, color=GREEN, fill_opacity=0.15, stroke_width=4).shift(RIGHT*3.5)
        syn_title = txt("Synthetic Text", scale=0.55, color=GREEN).move_to(syn_box.get_top()+UP*0.3)
        syn_content = txt("A patient has a\nserious medical condition.\nTheir treatment plan\ninvolves ongoing care.", scale=0.4, color=GREEN, line_spacing=0.5).move_to(syn_box)

        play_sync(Create(real_box), Write(real_title), Write(real_content), run_time=1.2)
        play_sync(Create(syn_box), Write(syn_title), Write(syn_content), run_time=1.2)
        wait_until(T_END_COMPARE)

        # ----- Xóa hai khung so sánh trước khi hiện kết luận -----
        play_sync(FadeOut(real_box), FadeOut(real_title), FadeOut(real_content),
                  FadeOut(syn_box), FadeOut(syn_title), FadeOut(syn_content), run_time=0.8)
        wait_until(T_END_CONCLUSION - 0.5)

        # ----- Câu kết luận -----
        conclusion = txt("Both DP-SGD and Private Evolution are powerful tools.\nChoose based on your resources and privacy requirements.",
                         scale=0.45, line_spacing=0.5)
        conclusion.move_to(ORIGIN)
        play_sync(Write(conclusion), run_time=2.0)
        wait_until(T_END_FINAL - 1.0)

        # ----- Thông điệp cuối -----
        final_msg = txt("Protect Privacy, Unlock Data", scale=0.6, color=YELLOW, weight="BOLD")
        final_msg.to_edge(DOWN)
        play_sync(Write(final_msg), run_time=1.2)
        wait_until(T_END_FINAL)

        self.wait(1)
        play_sync(FadeOut(conclusion), FadeOut(final_msg), FadeOut(result_title), run_time=0.5)
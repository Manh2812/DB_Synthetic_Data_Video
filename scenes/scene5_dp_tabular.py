from manim import *
import numpy as np
import random

class Scene5Tabular(Scene):
    def construct(self):
        font_main = "Arial"
        color_real = BLUE
        color_synth = ORANGE

        # =============================================================
        # PHÂN CẢNH 1: DỮ LIỆU NHẠY CẢM
        # =============================================================
        title1 = Text("Phase 5: DP Synthetic Tabular Data", font=font_main, font_size=36).to_edge(UP)
        subtitle1 = Text("Handling Sensitive Healthcare Records", font=font_main, font_size=24,
                         color=color_real).next_to(title1, DOWN)

        table_real = Table(
            [["45", "2000$", "Cancer"],
             ["30", "1500$", "Flu"],
             ["60", "1200$", "Diabetes"],
             ["25", "3000$", "Healthy"],
             ["52", "2500$", "Heart D."]],
            col_labels=[Text("Age"), Text("Income"), Text("Disease")],
            include_outer_lines=True
        ).scale(0.5).shift(DOWN * 0.5)

        self.play(Write(title1), run_time=2)
        self.play(FadeIn(subtitle1), run_time=2)
        self.wait(1)

        # Vẽ bảng (từng phần)
        self.play(Create(table_real.get_horizontal_lines()), run_time=2)
        self.play(Create(table_real.get_vertical_lines()), run_time=2)
        self.play(FadeIn(table_real.get_rows()), run_time=3)
        self.wait(2)

        highlight_rect = SurroundingRectangle(table_real.get_rows()[1], color=RED)
        warning_text = Text("High Re-identification Risk!", font=font_main, font_size=24, color=RED).next_to(table_real, RIGHT)

        self.play(Create(highlight_rect), run_time=1.5)
        self.play(Write(warning_text), run_time=2)
        self.wait(5)

        self.play(FadeOut(warning_text), FadeOut(highlight_rect), FadeOut(subtitle1))
        self.play(table_real.get_rows()[1:].animate.set_opacity(0.1), run_time=2)
        self.wait(4)

        # =============================================================
        # PHÂN CẢNH 2: BAYESIAN NETWORK
        # =============================================================
        node_age = Circle(radius=0.7, color=color_real).shift(UP * 1.5)
        node_income = Circle(radius=1, color=color_real).shift(DOWN * 1 + LEFT * 2.5)
        node_disease = Circle(radius=1, color=color_real).shift(DOWN * 1 + RIGHT * 2.5)

        label_a = MathTex(r"\text{Age}").move_to(node_age)
        label_i = MathTex(r"\text{Income}").move_to(node_income)
        label_d = MathTex(r"\text{Disease}").move_to(node_disease)

        # Chuyển đổi cực chậm
        self.play(
            ReplacementTransform(table_real.get_cell((1, 1)), label_a),
            ReplacementTransform(table_real.get_cell((1, 2)), label_i),
            ReplacementTransform(table_real.get_cell((1, 3)), label_d),
            Create(node_age), Create(node_income), Create(node_disease),
            table_real.animate.shift(DOWN * 10),
            run_time=4
        )
        self.wait(2)

        arrow_ai = Arrow(node_age.get_bottom(), node_income.get_top(), color=WHITE)
        arrow_ad = Arrow(node_age.get_bottom(), node_disease.get_top(), color=WHITE)
        prob_ai = MathTex(r"P(\text{Income}|\text{Age})", font_size=24).next_to(arrow_ai, LEFT, buff=0.2)
        prob_ad = MathTex(r"P(\text{Disease}|\text{Age})", font_size=24).next_to(arrow_ad, RIGHT, buff=0.2)

        self.play(GrowArrow(arrow_ai), run_time=2)
        self.play(Write(prob_ai), run_time=2)
        self.play(GrowArrow(arrow_ad), run_time=2)
        self.play(Write(prob_ad), run_time=2)
        self.wait(4)

        # =============================================================
        # PHÂN CẢNH 3: PRIVBAYES & NOISE
        # =============================================================
        epsilon = MathTex(r"\epsilon \text{ (Privacy Budget)}", font_size=40, color=YELLOW).to_edge(RIGHT, buff=1)
        self.play(Write(epsilon), run_time=2)
        self.wait(2)

        # Tạo nhiễu thành 2 đợt
        for _ in range(2):
            noise_dots = VGroup(*[Dot(radius=0.05, color=random.choice([YELLOW, WHITE, BLUE_A])) for _ in range(20)])
            noise_dots.move_to(epsilon.get_center())
            self.play(
                *[dot.animate.move_to(
                    random.choice([arrow_ai, arrow_ad]).point_from_proportion(random.random()) + np.random.randn(3) * 0.4
                ) for dot in noise_dots],
                run_time=3,
                rate_func=bezier([0, 0, 1, 1])
            )
            self.play(FadeOut(noise_dots), run_time=1)

        self.play(Indicate(prob_ai, color=YELLOW), Indicate(prob_ad, color=YELLOW), run_time=2)
        self.play(Flash(epsilon, color=YELLOW, flash_radius=0.5), run_time=2)
        self.wait(5)

        # =============================================================
        # PHÂN CẢNH 4: SINH DỮ LIỆU TỔNG HỢP
        # =============================================================
        bayes_net = VGroup(node_age, node_income, node_disease, label_a, label_i, label_d, arrow_ai, arrow_ad, prob_ai, prob_ad, epsilon)
        self.play(bayes_net.animate.scale(0.7).to_edge(LEFT, buff=0.5), run_time=3)

        table_synth = Table(
            [["44", "2100$", "Cancer"],
             ["31", "1450$", "Flu"],
             ["59", "1250$", "Diabetes"],
             ["26", "2900$", "Healthy"],
             ["53", "2550$", "Heart D."]],
            col_labels=[Text("Age"), Text("Income"), Text("Disease")],
            include_outer_lines=True
        ).scale(0.4).to_edge(RIGHT, buff=0.5)

        synth_title = Text("DP Synthetic Data", font=font_main, font_size=28, color=color_synth).next_to(table_synth, UP)
        self.play(Write(synth_title), Create(table_synth.get_horizontal_lines()),
                  Create(table_synth.get_vertical_lines()), run_time=3)

        # Sinh từng hàng
        for i in range(1, 6):
            line = Line(bayes_net.get_right(), table_synth.get_rows()[i].get_left(), color=color_synth, stroke_width=2)
            self.play(ShowPassingFlash(line), run_time=0.8)
            self.play(FadeIn(table_synth.get_rows()[i]), run_time=0.8)
            self.wait(0.5)

        self.wait(4)

        # =============================================================
        # PHÂN CẢNH 5: SO SÁNH & KẾT LUẬN
        # =============================================================
        self.play(
            bayes_net.animate.scale(0.5).to_corner(UL),
            VGroup(table_synth, synth_title).animate.scale(0.7).to_corner(UR),
            run_time=3
        )

        axes = Axes(x_range=[0, 10], y_range=[0, 5], x_length=5, y_length=2.5).shift(DOWN)
        curve_real = axes.plot(lambda x: 4 * np.exp(-0.5 * (x - 3) ** 2), color=color_real)
        curve_synth = axes.plot(lambda x: 3.8 * np.exp(-0.48 * (x - 3.1) ** 2), color=color_synth)

        self.play(Create(axes), Create(curve_real), run_time=3)
        self.wait(1)
        self.play(Create(curve_synth), run_time=4)

        shield = RegularPolygon(n=6, color=WHITE).scale(0.7).move_to(axes.get_center())
        shield_text = Text("SECURE", font=font_main, font_size=20).move_to(shield.get_center())

        self.play(Create(shield), Write(shield_text), run_time=2)
        self.play(Indicate(shield, color=GREEN), run_time=2)

        final_msg = Text("Protect Privacy, Unlock Data", font=font_main, font_size=32).to_edge(DOWN)
        self.play(Write(final_msg), run_time=3)

        self.wait(6)

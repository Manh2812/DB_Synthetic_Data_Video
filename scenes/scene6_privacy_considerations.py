from manim import *

config.background_color = BLACK
config.pixel_width = 1920
config.pixel_height = 1080


def txt(content, scale=0.5, color=WHITE):
    return Text(content, font="Arial", color=color).scale(scale)


def title(content, scale=0.72, color=WHITE):
    return Text(content, font="Arial", color=color).scale(scale)


def pill(content, color=WHITE, scale=0.42):
    box = RoundedRectangle(width=3.2, height=0.8, corner_radius=0.18, color=color, stroke_width=3)
    label = txt(content, scale=scale, color=color).move_to(box)
    return VGroup(box, label)


def glowing_dot(point, color=BLUE):
    outer = Circle(radius=0.18, color=color, stroke_width=2, fill_opacity=0.08).move_to(point)
    inner = Dot(point=point, radius=0.055, color=color)
    return VGroup(outer, inner)


class PrivacyConsiderations(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        question = title("Is synthetic data actually safe to release?", scale=0.62)
        question.move_to(ORIGIN)
        self.play(Write(question), run_time=1.5)
        self.wait(0.6)
        self.play(question.animate.to_edge(UP, buff=0.55).scale(0.78), run_time=0.9)

        guide = Line(LEFT * 5.1, RIGHT * 5.1, color=GRAY_B, stroke_width=2).to_edge(UP, buff=1.35)
        guide_dots = VGroup(*[
            glowing_dot(guide.point_from_proportion(i / 4), color)
            for i, color in enumerate([BLUE, RED, YELLOW, GREEN, BLUE])
        ])
        tracker = Dot(guide.get_start(), color=WHITE, radius=0.07)
        self.play(Create(guide), LaggedStart(*[FadeIn(dot) for dot in guide_dots], lag_ratio=0.08), FadeIn(tracker), run_time=1.0)

        # =====================================================
        # PRIVACY VS UTILITY
        # =====================================================

        beam = Line(LEFT * 3.5, RIGHT * 3.5, color=WHITE, stroke_width=5)
        pivot = Triangle(color=WHITE, stroke_width=4, fill_opacity=0).scale(0.35).rotate(PI)
        pivot.next_to(beam, DOWN, buff=0)

        privacy = txt("Privacy", scale=0.58, color=BLUE)
        utility = txt("Utility", scale=0.58, color=YELLOW)
        privacy.next_to(beam.get_left(), DOWN, buff=0.42)
        utility.next_to(beam.get_right(), DOWN, buff=0.42)

        eps = MathTex(r"\varepsilon", color=WHITE).scale(1.2).to_edge(DOWN, buff=0.62)
        eps_note = txt("smaller", scale=0.38, color=BLUE).next_to(eps, LEFT, buff=0.35)
        eps_note_2 = txt("larger", scale=0.38, color=YELLOW).next_to(eps, RIGHT, buff=0.35)

        self.play(Create(beam), Create(pivot), FadeIn(privacy), FadeIn(utility), Write(eps), run_time=1.4)
        self.play(FadeIn(eps_note), beam.animate.rotate(10 * DEGREES, about_point=ORIGIN), run_time=1.2)
        self.play(Transform(eps_note, eps_note_2), beam.animate.rotate(-22 * DEGREES, about_point=ORIGIN), run_time=1.35)

        tradeoff = txt("trade-off", scale=0.48, color=GREEN).to_edge(DOWN, buff=0.62)
        self.play(Transform(eps_note, tradeoff), FadeOut(eps), run_time=0.8)
        self.wait(0.6)

        self.play(
            FadeOut(VGroup(beam, pivot, privacy, utility, eps_note), shift=LEFT * 0.4),
            tracker.animate.move_to(guide.point_from_proportion(0.25)),
            run_time=0.9,
        )

        # =====================================================
        # MEMBERSHIP INFERENCE
        # =====================================================

        training = RoundedRectangle(width=3.4, height=2.0, corner_radius=0.15, color=BLUE, stroke_width=3).shift(LEFT * 4.25)
        generator = RoundedRectangle(width=2.8, height=1.15, corner_radius=0.15, color=GREEN, stroke_width=3)
        synthetic = RoundedRectangle(width=3.4, height=2.0, corner_radius=0.15, color=YELLOW, stroke_width=3).shift(RIGHT * 4.25)

        train_rows = VGroup(
            txt("Alice", scale=0.5),
            txt("age 47", scale=0.4),
            txt("cancer", scale=0.4),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).move_to(training)
        gen_label = txt("DP generator", scale=0.43, color=GREEN).move_to(generator)
        synth_rows = VGroup(
            txt("age 46 | cancer", scale=0.35),
            txt("age 51 | diabetes", scale=0.35),
            txt("age 48 | cancer", scale=0.35),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).move_to(synthetic)

        arrow_1 = Arrow(training.get_right(), generator.get_left(), buff=0.15)
        arrow_2 = Arrow(generator.get_right(), synthetic.get_left(), buff=0.15)

        self.play(Create(training), Write(train_rows), run_time=1.0)
        self.play(Create(generator), Write(gen_label), GrowArrow(arrow_1), run_time=1.0)
        self.play(Create(synthetic), Write(synth_rows), GrowArrow(arrow_2), run_time=1.0)

        attacker = txt("Attacker", scale=0.55, color=RED).to_corner(DR)
        question_mark = MathTex(r"\text{Alice?}", color=RED).scale(0.8).next_to(attacker, UP, buff=0.25)
        attack_arrow = CurvedArrow(synthetic.get_bottom(), attacker.get_top(), color=RED, angle=PI / 4)
        confidence_bar = Rectangle(width=2.8, height=0.18, color=RED, fill_color=RED, fill_opacity=0.7)
        confidence_bar.to_edge(DOWN, buff=0.72)
        confidence_label = txt("confidence", scale=0.35, color=RED).next_to(confidence_bar, UP, buff=0.15)

        self.play(FadeIn(attacker), Write(question_mark), Create(attack_arrow), run_time=1.0)
        self.play(FadeIn(confidence_label), GrowFromEdge(confidence_bar, LEFT), run_time=0.8)

        short_bar = Rectangle(width=1.25, height=0.18, color=GREEN, fill_color=GREEN, fill_opacity=0.7)
        short_bar.align_to(confidence_bar, LEFT).move_to(confidence_bar.get_left() + RIGHT * 0.625)
        shield = SurroundingRectangle(generator, color=GREEN, buff=0.15, stroke_width=4)
        limited = txt("limited influence", scale=0.42, color=GREEN).next_to(generator, DOWN, buff=0.35)

        self.play(Create(shield), Transform(confidence_bar, short_bar), FadeOut(attack_arrow), run_time=1.2)
        self.play(FadeIn(limited), run_time=0.6)
        self.wait(0.6)

        self.play(
            FadeOut(VGroup(training, train_rows, generator, gen_label, synthetic, synth_rows, arrow_1, arrow_2, attacker, question_mark, confidence_bar, confidence_label, shield, limited), shift=LEFT * 0.35),
            tracker.animate.move_to(guide.point_from_proportion(0.5)),
            run_time=0.9,
        )

        # =====================================================
        # RE-IDENTIFICATION
        # =====================================================

        synthetic_card = Rectangle(width=4.5, height=2.35, color=YELLOW, stroke_width=3).shift(LEFT * 3.15)
        public_card = Rectangle(width=3.8, height=1.85, color=BLUE, stroke_width=3).shift(RIGHT * 3.3)

        synth_label = txt("synthetic record", scale=0.42, color=YELLOW).next_to(synthetic_card, UP, buff=0.22)
        public_label = txt("public records", scale=0.42, color=BLUE).next_to(public_card, UP, buff=0.22)
        synth_data = VGroup(
            txt("age: 47", scale=0.43),
            txt("ZIP: 90210", scale=0.43),
            txt("disease: diabetes", scale=0.43),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).move_to(synthetic_card)
        public_data = VGroup(
            txt("age 47", scale=0.48),
            txt("ZIP 90210", scale=0.48),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).move_to(public_card)

        self.play(Create(synthetic_card), FadeIn(synth_label), Write(synth_data), run_time=1.0)
        self.play(Create(public_card), FadeIn(public_label), Write(public_data), run_time=0.9)

        links = VGroup(
            Arrow(public_card.get_left(), synthetic_card.get_right() + UP * 0.35, buff=0.1, color=RED),
            Arrow(public_card.get_left() + DOWN * 0.35, synthetic_card.get_right() + DOWN * 0.3, buff=0.1, color=RED),
        )
        risk = txt("re-identification", scale=0.48, color=RED).to_edge(DOWN, buff=0.62)
        dp_blur = txt("blurred linkage", scale=0.42, color=GREEN).next_to(synthetic_card, DOWN, buff=0.32)
        dp_ring = SurroundingRectangle(synthetic_card, color=GREEN, buff=0.14, stroke_width=4)

        self.play(LaggedStart(*[GrowArrow(link) for link in links], lag_ratio=0.15), Write(risk), run_time=1.1)
        self.play(Create(dp_ring), links.animate.set_opacity(0.25), Transform(risk, dp_blur), run_time=1.0)
        self.wait(0.6)

        self.play(
            FadeOut(VGroup(synthetic_card, public_card, synth_label, public_label, synth_data, public_data, links, risk, dp_ring), shift=LEFT * 0.35),
            tracker.animate.move_to(guide.point_from_proportion(0.75)),
            run_time=0.9,
        )

        # =====================================================
        # PRIVACY AUDITING
        # =====================================================

        dataset = RoundedRectangle(width=5.3, height=2.5, corner_radius=0.15, color=WHITE, stroke_width=3).shift(LEFT * 2.8)
        rows = VGroup(
            txt("sample_01   age 46   disease A", scale=0.34),
            txt("sample_02   age 51   disease B", scale=0.34),
            txt("sample_03   age 48   disease A", scale=0.34),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14).move_to(dataset)

        lens = VGroup(
            Circle(radius=0.68, color=BLUE, stroke_width=4),
            Line(DOWN * 0.5 + RIGHT * 0.5, DOWN * 1.05 + RIGHT * 1.05, color=BLUE, stroke_width=5),
        ).shift(RIGHT * 2.4 + UP * 0.4)
        scan_line = Line(dataset.get_top(), dataset.get_bottom(), color=BLUE, stroke_width=4).move_to(dataset.get_left() + RIGHT * 0.55)

        tests = VGroup(
            txt("membership", scale=0.36, color=GREEN),
            txt("reconstruction", scale=0.36, color=GREEN),
            txt("leakage", scale=0.36, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28).shift(RIGHT * 3.2 + DOWN * 0.15)

        self.play(Create(dataset), Write(rows), FadeIn(lens), run_time=1.1)
        self.play(Create(scan_line), run_time=0.5)

        for i, test in enumerate(tests):
            target_x = dataset.get_left()[0] + 1.15 + i * 1.05
            target = np.array([target_x, dataset.get_center()[1], 0])
            self.play(
                scan_line.animate.move_to(target),
                lens.animate.shift(RIGHT * 0.28 + DOWN * 0.05),
                run_time=0.65,
            )
            pulse = Dot(point=dataset.get_right() + RIGHT * 0.32 + UP * (0.35 - i * 0.35), color=GREEN, radius=0.055)
            self.play(FadeIn(test), FadeIn(pulse), Indicate(pulse, color=GREEN, scale_factor=1.25), run_time=0.55)

        needs_testing = txt("needs testing", scale=0.48, color=WHITE).to_edge(DOWN, buff=0.62)
        self.play(Write(needs_testing), run_time=0.8)
        self.wait(0.6)

        self.play(
            FadeOut(VGroup(dataset, rows, lens, scan_line, tests, needs_testing), shift=LEFT * 0.35),
            tracker.animate.move_to(guide.point_from_proportion(1.0)),
            run_time=0.9,
        )

        # =====================================================
        # EVALUATION AND RELEASE
        # =====================================================

        tri = Polygon(
            UP * 2.1,
            LEFT * 2.45 + DOWN * 1.75,
            RIGHT * 2.45 + DOWN * 1.75,
            color=WHITE,
            stroke_width=3,
        )
        privacy_label = txt("Privacy", scale=0.5, color=GREEN).move_to(UP * 2.48)
        utility_label = txt("Utility", scale=0.5, color=BLUE).move_to(LEFT * 3.05 + DOWN * 2.1)
        fidelity_label = txt("Fidelity", scale=0.5, color=YELLOW).move_to(RIGHT * 3.05 + DOWN * 2.1)

        point = Dot(point=LEFT * 0.35 + DOWN * 0.25, radius=0.08, color=RED)
        path = VMobject(color=RED, stroke_width=3).set_points_as_corners([
            LEFT * 0.35 + DOWN * 0.25,
            LEFT * 0.85 + UP * 0.15,
            RIGHT * 0.75 + DOWN * 0.15,
            DOWN * 0.62,
        ])
        balance = txt("balance", scale=0.45, color=GREEN).next_to(Dot(DOWN * 0.62), RIGHT, buff=0.25)

        self.play(Create(tri), FadeIn(privacy_label), FadeIn(utility_label), FadeIn(fidelity_label), run_time=1.2)
        self.play(FadeIn(point), run_time=0.4)
        self.play(MoveAlongPath(point, path), Create(path), run_time=2.2)
        self.play(FadeIn(balance), run_time=0.5)
        self.wait(0.5)

        self.play(FadeOut(VGroup(tri, privacy_label, utility_label, fidelity_label, point, path, balance), shift=UP * 0.2), run_time=0.8)

        pipeline = VGroup(
            RoundedRectangle(width=1.9, height=0.75, corner_radius=0.12, color=BLUE, stroke_width=3),
            RoundedRectangle(width=1.9, height=0.75, corner_radius=0.12, color=GREEN, stroke_width=3),
            RoundedRectangle(width=1.9, height=0.75, corner_radius=0.12, color=YELLOW, stroke_width=3),
            RoundedRectangle(width=1.9, height=0.75, corner_radius=0.12, color=WHITE, stroke_width=3),
            RoundedRectangle(width=1.9, height=0.75, corner_radius=0.12, color=GREEN, stroke_width=3),
        ).arrange(RIGHT, buff=0.28).shift(DOWN * 0.25)

        labels = VGroup(
            txt("Raw data", scale=0.36, color=BLUE).move_to(pipeline[0]),
            txt("DP train", scale=0.36, color=GREEN).move_to(pipeline[1]),
            txt("Synthetic", scale=0.36, color=YELLOW).move_to(pipeline[2]),
            txt("Audit", scale=0.36, color=WHITE).move_to(pipeline[3]),
            txt("Release", scale=0.36, color=GREEN).move_to(pipeline[4]),
        )
        arrows = VGroup(*[
            Arrow(pipeline[i].get_right(), pipeline[i + 1].get_left(), buff=0.07, color=WHITE)
            for i in range(len(pipeline) - 1)
        ])

        self.play(LaggedStart(*[Create(box) for box in pipeline], lag_ratio=0.12), run_time=1.1)
        self.play(LaggedStart(*[FadeIn(label) for label in labels], lag_ratio=0.08), run_time=0.8)
        self.play(LaggedStart(*[GrowArrow(arr) for arr in arrows], lag_ratio=0.12), run_time=1.0)

        finale = title("Safe and useful synthetic data", scale=0.68, color=GREEN).to_edge(DOWN, buff=0.62)
        self.play(Write(finale), run_time=1.0)
        self.wait(1.8)

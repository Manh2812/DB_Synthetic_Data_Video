import os
from manim import *


class Scene1Intro(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        AUDIO_CANDIDATES = [
            "assets/audio/scene1_intro.mp3",
        ]

        for audio_path in AUDIO_CANDIDATES:
            if os.path.exists(audio_path):
                self.add_sound(audio_path)
                break

        # =========================================================
        # TIMELINE HELPERS
        # Audio length ~72.3s
        # =========================================================
        clock = {"t": 0.0}

        def play_sync(*animations, run_time=1.0, **kwargs):
            self.play(*animations, run_time=run_time, **kwargs)
            clock["t"] += run_time

        def wait_until(target_time):
            gap = target_time - clock["t"]
            if gap > 0:
                self.wait(gap)
                clock["t"] = target_time

        # =========================================================
        # STYLE HELPERS
        # =========================================================
        FONT = "Arial"

        def txt(content, scale=0.5, color=WHITE, weight="NORMAL"):
            return Text(content, font=FONT, color=color, weight=weight).scale(scale)

        def safe_formula():
            try:
                return MathTex(
                    r"\mathcal{D}\ \longrightarrow\ f_{\theta}\ \longrightarrow\ \hat{y}",
                    color=WHITE
                ).scale(0.82)
            except Exception:
                return txt("Dataset -> Model -> Prediction", scale=0.50)

        def make_text_card(title, lines):
            box = RoundedRectangle(
                corner_radius=0.16,
                width=3.45,
                height=2.15,
                stroke_color=WHITE,
                stroke_width=1.8,
            ).set_fill(GREY_E, opacity=0.14)

            header = txt(title, scale=0.50, weight="BOLD")
            header.move_to(box.get_top() + DOWN * 0.35)

            body = VGroup(*[
                txt(line, scale=0.31)
                for line in lines
            ]).arrange(DOWN, aligned_edge=LEFT, buff=0.10)
            body.move_to(box.get_center() + DOWN * 0.12)

            return VGroup(box, header, body)

        def make_icon_card(title, icon, lines):
            box = RoundedRectangle(
                corner_radius=0.16,
                width=3.45,
                height=2.15,
                stroke_color=WHITE,
                stroke_width=1.8,
            ).set_fill(GREY_E, opacity=0.14)

            header = txt(title, scale=0.50, weight="BOLD")
            header.move_to(box.get_top() + DOWN * 0.35)

            icon.move_to(box.get_center() + UP * 0.18)

            body = VGroup(*[
                txt(line, scale=0.26)
                for line in lines
            ]).arrange(DOWN, buff=0.05)
            body.move_to(box.get_center() + DOWN * 0.60)

            return VGroup(box, header, icon, body)

        def image_icon():
            frame = Rectangle(width=1.00, height=0.62, stroke_color=WHITE, stroke_width=1.5)
            sun = Dot(point=UP * 0.16 + RIGHT * 0.23, radius=0.04, color=WHITE)
            mountain1 = Polygon(
                LEFT * 0.36 + DOWN * 0.18,
                LEFT * 0.08 + UP * 0.06,
                RIGHT * 0.10 + DOWN * 0.18,
                color=WHITE,
                stroke_width=1.5,
            )
            mountain2 = Polygon(
                LEFT * 0.02 + DOWN * 0.18,
                RIGHT * 0.18 + UP * 0.02,
                RIGHT * 0.36 + DOWN * 0.18,
                color=WHITE,
                stroke_width=1.5,
            )
            return VGroup(frame, sun, mountain1, mountain2)

        def table_icon():
            grid = VGroup()
            w, h = 1.02, 0.62
            xs = [-w / 2, -w / 6, w / 6, w / 2]
            ys = [-h / 2, -h / 6, h / 6, h / 2]
            for x in xs:
                grid.add(Line(
                    UP * h / 2 + RIGHT * x,
                    DOWN * h / 2 + RIGHT * x,
                    color=WHITE,
                    stroke_width=1.3,
                ))
            for y in ys:
                grid.add(Line(
                    LEFT * w / 2 + UP * y,
                    RIGHT * w / 2 + UP * y,
                    color=WHITE,
                    stroke_width=1.3,
                ))
            return grid

        def make_model_box(label="Model"):
            box = RoundedRectangle(
                corner_radius=0.18,
                width=2.25,
                height=1.15,
                stroke_color=WHITE,
                stroke_width=1.8,
            ).set_fill(GREY_E, opacity=0.16)
            label_obj = txt(label, scale=0.56, weight="BOLD")
            label_obj.move_to(box.get_center())
            return VGroup(box, label_obj)

        def make_prediction_box():
            box = RoundedRectangle(
                corner_radius=0.18,
                width=2.70,
                height=1.15,
                stroke_color=WHITE,
                stroke_width=1.8,
            ).set_fill(GREY_E, opacity=0.16)
            label_obj = txt("Prediction", scale=0.50, weight="BOLD")
            label_obj.move_to(box.get_center())
            return VGroup(box, label_obj)

        def dataset_icon():
            dots = VGroup()
            for _ in range(16):
                dots.add(Dot(radius=0.045, color=WHITE))
            dots.arrange_in_grid(rows=4, cols=4, buff=0.14)
            return dots

        def labeled_box(title, subtitle, color, width=3.10, height=1.25):
            box = RoundedRectangle(
                corner_radius=0.18,
                width=width,
                height=height,
                stroke_color=color,
                stroke_width=1.8,
            ).set_fill(color, opacity=0.10)

            title_obj = txt(title, scale=0.46, color=color, weight="BOLD")
            subtitle_obj = txt(subtitle, scale=0.28, color=WHITE)

            title_obj.move_to(box.get_center() + UP * 0.16)
            subtitle_obj.move_to(box.get_center() + DOWN * 0.20)

            return VGroup(box, title_obj, subtitle_obj)

        def warning_icon():
            tri = Triangle(color=RED_C, stroke_width=2.0).scale(0.30)
            tri.set_fill(RED_E, opacity=0.12)
            mark = txt("!", scale=0.42, color=RED_C, weight="BOLD")
            mark.move_to(tri.get_center() + DOWN * 0.02)
            return VGroup(tri, mark)

        # =========================================================
        # 0.00 - 4.58
        # OPENING
        # =========================================================
        title = txt("Data powers Machine Learning", scale=0.70, weight="BOLD")
        title.move_to(UP * 2.65)

        subtitle = txt("Data is what a model learns from", scale=0.37)
        subtitle.next_to(title, DOWN, buff=0.25)

        play_sync(Write(title), run_time=2.2)
        play_sync(FadeIn(subtitle, shift=UP * 0.10), run_time=0.8)
        wait_until(4.58)

        # =========================================================
        # 4.58 - 11.30
        # MODEL WITHOUT DATA
        # =========================================================
        model_empty = make_model_box("Model")
        model_empty.move_to(LEFT * 2.25 + DOWN * 0.15)

        unknown_outputs = VGroup(
            txt("classify image?", scale=0.31),
            txt("predict disease?", scale=0.31),
            txt("estimate risk?", scale=0.31),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        unknown_outputs.move_to(RIGHT * 2.65 + DOWN * 0.05)

        q_marks = VGroup(
            txt("?", scale=0.52),
            txt("?", scale=0.52),
            txt("?", scale=0.52),
        ).arrange(DOWN, buff=0.18)
        q_marks.next_to(unknown_outputs, LEFT, buff=0.30)

        arrow_uncertain = Arrow(
            model_empty.get_right(),
            q_marks.get_left(),
            buff=0.18,
            color=GREY_B,
            stroke_width=1.5,
        )

        play_sync(FadeOut(subtitle), FadeIn(model_empty, shift=UP * 0.10), run_time=1.2)
        play_sync(GrowArrow(arrow_uncertain), FadeIn(q_marks), FadeIn(unknown_outputs), run_time=1.5)

        no_data_label = txt("No data, no learning", scale=0.40, color=YELLOW_C)
        no_data_label.next_to(model_empty, DOWN, buff=0.33)
        play_sync(FadeIn(no_data_label), run_time=1.0)

        wait_until(11.30)

        # =========================================================
        # 11.30 - 30.19
        # DATA TYPES
        # =========================================================
        play_sync(
            FadeOut(model_empty),
            FadeOut(arrow_uncertain),
            FadeOut(q_marks),
            FadeOut(unknown_outputs),
            FadeOut(no_data_label),
            FadeOut(title),
            run_time=0.8
        )

        section_title = txt("Data comes in many forms", scale=0.62, weight="BOLD")
        section_title.move_to(UP * 2.80)

        text_card = make_text_card("Text", ["medical note", "chat message", "email"])
        image_card = make_icon_card("Image", image_icon(), ["X-ray", "avatar", "camera photo"])
        tabular_card = make_icon_card("Tabular", table_icon(), ["age", "income", "health status"])

        cards = VGroup(text_card, image_card, tabular_card).arrange(RIGHT, buff=0.55)
        cards.move_to(UP * 0.10)

        examples = VGroup(
            txt("medical records", scale=0.29),
            txt("user profiles", scale=0.29),
            txt("financial data", scale=0.29),
        ).arrange(RIGHT, buff=0.95)
        examples.next_to(cards, DOWN, buff=0.55)

        play_sync(FadeIn(section_title), run_time=0.8)
        play_sync(
            LaggedStart(
                FadeIn(text_card, shift=UP * 0.12),
                FadeIn(image_card, shift=UP * 0.12),
                FadeIn(tabular_card, shift=UP * 0.12),
                lag_ratio=0.18,
            ),
            run_time=2.0
        )
        play_sync(FadeIn(examples, shift=UP * 0.08), run_time=1.0)

        wait_until(15.74)
        play_sync(Circumscribe(text_card[0], color=YELLOW_C, stroke_width=2.2), run_time=1.4)

        wait_until(19.08)
        play_sync(Circumscribe(image_card[0], color=YELLOW_C, stroke_width=2.2), run_time=1.4)

        wait_until(23.43)
        play_sync(Circumscribe(tabular_card[0], color=YELLOW_C, stroke_width=2.2), run_time=1.4)

        wait_until(29.00)

        compact_data = VGroup(
            dataset_icon(),
            txt("Dataset", scale=0.40, weight="BOLD")
        ).arrange(DOWN, buff=0.28)
        compact_data.move_to(LEFT * 4.80 + DOWN * 0.15)

        play_sync(
            FadeOut(cards),
            FadeOut(examples),
            FadeIn(compact_data, shift=RIGHT * 0.12),
            run_time=1.1
        )

        wait_until(30.19)

        # =========================================================
        # 30.19 - 37.98
        # DATA -> MODEL -> PREDICTION
        # =========================================================
        play_sync(FadeOut(section_title), run_time=0.4)

        formula = safe_formula()
        formula.move_to(UP * 2.52)

        model = make_model_box("Model")
        model.move_to(ORIGIN + DOWN * 0.05)

        prediction = make_prediction_box()
        prediction.move_to(RIGHT * 4.15 + DOWN * 0.05)

        arrow_data_model = Arrow(
            compact_data.get_right(),
            model.get_left(),
            buff=0.22,
            color=WHITE,
            stroke_width=1.6,
        )
        arrow_model_pred = Arrow(
            model.get_right(),
            prediction.get_left(),
            buff=0.22,
            color=WHITE,
            stroke_width=1.6,
        )

        pred_examples = VGroup(
            txt("classify image", scale=0.28),
            txt("diagnose disease", scale=0.28),
            txt("estimate risk", scale=0.28),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.10)
        pred_examples.next_to(prediction, DOWN, buff=0.20)

        play_sync(FadeIn(model), GrowArrow(arrow_data_model), run_time=1.8)
        play_sync(
            FadeIn(formula),
            FadeIn(prediction),
            GrowArrow(arrow_model_pred),
            run_time=1.6
        )
        play_sync(FadeIn(pred_examples, shift=UP * 0.08), run_time=0.9)

        wait_until(37.98)

        # =========================================================
        # 37.98 - 44.83
        # PATTERN + IDENTITY
        # =========================================================
        play_sync(
            FadeOut(formula),
            FadeOut(arrow_data_model),
            FadeOut(arrow_model_pred),
            FadeOut(pred_examples),
            FadeOut(prediction),
            FadeOut(model),
            FadeOut(compact_data),
            run_time=0.8
        )

        idea_title = txt("Real data contains two things", scale=0.56, weight="BOLD")
        idea_title.move_to(UP * 2.65)

        real_data = labeled_box("Real data", "", WHITE, width=2.70, height=1.05)
        real_data[2].set_opacity(0)  # ẩn subtitle trống
        real_data.move_to(LEFT * 4.30)

        pattern_group = labeled_box("Pattern", "useful for ML", YELLOW_C, width=3.00, height=1.25)
        pattern_group.move_to(RIGHT * 1.65 + UP * 0.95)

        identity_group = labeled_box("Identity", "privacy risk", RED_C, width=3.00, height=1.25)
        identity_group.move_to(RIGHT * 1.65 + DOWN * 0.95)

        arrow_pattern = Arrow(
            real_data.get_right(),
            pattern_group.get_left(),
            buff=0.20,
            color=YELLOW_C,
            stroke_width=1.7,
        )
        arrow_identity = Arrow(
            real_data.get_right(),
            identity_group.get_left(),
            buff=0.20,
            color=RED_C,
            stroke_width=1.7,
        )

        play_sync(FadeIn(idea_title), run_time=0.6)
        play_sync(FadeIn(real_data, shift=RIGHT * 0.10), run_time=0.8)
        play_sync(GrowArrow(arrow_pattern), FadeIn(pattern_group, shift=UP * 0.10), run_time=1.2)
        play_sync(GrowArrow(arrow_identity), FadeIn(identity_group, shift=DOWN * 0.10), run_time=1.2)

        wait_until(44.83)

        # =========================================================
        # 44.83 - 58.31
        # PRIVACY RISK
        # =========================================================
        play_sync(
            FadeOut(idea_title),
            FadeOut(real_data),
            FadeOut(pattern_group),
            FadeOut(identity_group),
            FadeOut(arrow_pattern),
            FadeOut(arrow_identity),
            run_time=0.8
        )

        warning_group = VGroup(
            warning_icon(),
            txt("Privacy Risk", scale=0.58, color=RED_C, weight="BOLD")
        ).arrange(RIGHT, buff=0.20)
        warning_group.move_to(UP * 2.55)

        record_box = RoundedRectangle(
            corner_radius=0.16,
            width=6.25,
            height=1.55,
            stroke_color=RED_C,
            stroke_width=1.9,
        ).set_fill(RED_E, opacity=0.10)

        col1 = VGroup(
            txt("name", scale=0.25, color=GREY_B),
            txt("John", scale=0.40, weight="BOLD")
        ).arrange(DOWN, buff=0.18)

        col2 = VGroup(
            txt("diagnosis", scale=0.25, color=GREY_B),
            txt("cancer", scale=0.40, weight="BOLD")
        ).arrange(DOWN, buff=0.18)

        col3 = VGroup(
            txt("location", scale=0.25, color=GREY_B),
            txt("home address", scale=0.40, weight="BOLD")
        ).arrange(DOWN, buff=0.18)

        row_columns = VGroup(col1, col2, col3).arrange(RIGHT, buff=0.95, aligned_edge=UP)
        row_columns.move_to(record_box.get_center())

        sensitive_record = VGroup(record_box, row_columns)
        sensitive_record.move_to(LEFT * 1.35 + DOWN * 0.05)

        real_person_box = RoundedRectangle(
            corner_radius=0.14,
            width=2.05,
            height=0.82,
            stroke_color=RED_C,
            stroke_width=1.7,
        ).set_fill(RED_E, opacity=0.08)
        real_person_label = txt("Real person", scale=0.34, color=RED_C, weight="BOLD")
        real_person = VGroup(real_person_box, real_person_label)
        real_person.move_to(RIGHT * 4.75 + DOWN * 0.10)

        link_to_person = DashedLine(
            sensitive_record.get_right(),
            real_person.get_left(),
            dash_length=0.12,
            color=RED_C,
            stroke_width=1.6,
        )

        attacker_circle = Circle(radius=0.32, color=RED_C, stroke_width=1.7)
        attacker_q = txt("?", scale=0.52, color=RED_C, weight="BOLD")
        attacker_q.move_to(attacker_circle.get_center())
        attacker_label = txt("Attacker", scale=0.26, color=RED_C)
        attacker = VGroup(attacker_circle, attacker_q, attacker_label).arrange(DOWN, buff=0.06)
        attacker.move_to(RIGHT * 4.90 + DOWN * 2.00)

        attack_line = DashedLine(
            attacker.get_top(),
            sensitive_record.get_right() + DOWN * 0.45,
            dash_length=0.11,
            color=RED_C,
            stroke_width=1.5,
        )

        play_sync(FadeIn(warning_group, shift=UP * 0.08), run_time=0.9)
        play_sync(FadeIn(sensitive_record, shift=UP * 0.10), run_time=1.2)

        wait_until(50.47)
        play_sync(Create(link_to_person), FadeIn(real_person), run_time=1.2)

        wait_until(53.25)
        play_sync(FadeIn(attacker, shift=LEFT * 0.10), Create(attack_line), run_time=1.6)

        wait_until(58.31)

        # =========================================================
        # 58.31 - 66.14
        # CENTRAL QUESTION
        # =========================================================
        play_sync(
            FadeOut(warning_group),
            FadeOut(sensitive_record),
            FadeOut(real_person),
            FadeOut(link_to_person),
            FadeOut(attacker),
            FadeOut(attack_line),
            run_time=0.9
        )

        question_1 = txt("How can we learn patterns", scale=0.60, weight="BOLD")
        question_2 = txt("without exposing users?", scale=0.60, color=YELLOW_C, weight="BOLD")
        question = VGroup(question_1, question_2).arrange(DOWN, buff=0.20)
        question.move_to(ORIGIN + UP * 0.15)

        note = txt("Pattern should remain. Identity should not.", scale=0.33, color=GREY_B)
        note.next_to(question, DOWN, buff=0.50)

        play_sync(Write(question_1), run_time=1.6)
        play_sync(Write(question_2), run_time=1.4)
        play_sync(FadeIn(note, shift=UP * 0.08), run_time=0.8)

        wait_until(66.14)

        # =========================================================
        # 66.14 - 72.30
        # ENDING / BRIDGE
        # =========================================================
        play_sync(FadeOut(question), FadeOut(note), run_time=0.8)

        next_label = txt("Next", scale=0.36, color=GREY_B)
        dp_label = txt("Differential Privacy", scale=0.64, weight="BOLD")
        synth_label = txt("DP synthetic data", scale=0.46, color=YELLOW_C, weight="BOLD")

        ending_group = VGroup(next_label, dp_label, synth_label).arrange(DOWN, buff=0.18)
        ending_group.move_to(ORIGIN)

        play_sync(FadeIn(next_label), run_time=0.5)
        play_sync(FadeIn(dp_label, shift=UP * 0.08), run_time=0.9)
        play_sync(FadeIn(synth_label, shift=UP * 0.08), run_time=0.8)

        wait_until(70.10)

        final_msg = txt("Protect Privacy, Unlock Data", scale=0.60, weight="BOLD")
        final_msg.move_to(ORIGIN)

        play_sync(FadeOut(ending_group), FadeIn(final_msg), run_time=1.2)

        wait_until(72.30)
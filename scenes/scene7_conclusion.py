
from manim import *
from pathlib import Path
import numpy as np

# ================================================================
# Scene 7 - Conclusion & Complete System
# Voice-aligned version for Minh Quan AI audio.
#
# Audio duration: 81.685s
#
# Main alignment points found from the actual audio pauses:
# 0.0  - 6.75  : Opening
# 6.75 - 23.50 : Why we need a complete system
# 23.50- 40.00 : Pipeline steps
# 40.00- 47.40 : Evaluation before publishing
# 47.40- 62.20 : When to use / be careful
# 62.20- 72.40 : Privacy-utility tradeoff
# 72.40- 81.685: Final message
# ================================================================

config.background_color = BLACK

FONT = "Arial"
BG = BLACK
WHITE_TEXT = WHITE
MUTED = GREY_B
BLUE_DP = BLUE_C
GREEN_SYNTH = GREEN_C
YELLOW_EVAL = YELLOW_C
PURPLE_MODEL = PURPLE_C
RED_RISK = RED_C
ORANGE_DATA = ORANGE
CYAN_PUBLISH = TEAL_C


class Scene7Conclusion(Scene):
    AUDIO_DURATION = 81.685

    def construct(self):
        self.camera.background_color = BG
        self.try_add_voiceover()

        self.opening_title()
        self.recap_problem()
        self.complete_pipeline()
        self.evaluation_loop()
        self.when_to_use()
        self.privacy_utility_tradeoff()
        self.final_message()

        self.hold_until(self.AUDIO_DURATION)

    # ------------------------------------------------------------
    # Audio
    # ------------------------------------------------------------
    def try_add_voiceover(self):
        scene_dir = Path(__file__).resolve().parent
        project_root = scene_dir.parent

        candidates = [
            project_root / "assets" / "audio" / "Minh_Quân_Audio_Scene7.mp3",
        ]

        for path in candidates:
            if path.exists():
                resolved = path.resolve()
                self.add_sound(str(resolved), time_offset=0)
                print(f"[Scene7] Added voiceover: {resolved}")
                return

        print("[Scene7] Voiceover file not found. Expected: assets/audio/Minh_Quân_Audio_Scene7.mp3")

    # ------------------------------------------------------------
    # Timing / cleanup
    # ------------------------------------------------------------
    def hold_until(self, target_time):
        frame_duration = 1 / config.frame_rate
        remaining = target_time - self.time
        if remaining >= frame_duration:
            self.wait(remaining)

    def clean_screen(self, run_time=0.40):
        mobs = list(self.mobjects)
        if mobs:
            self.play(*[FadeOut(m) for m in mobs], run_time=run_time)
        self.remove(*list(self.mobjects))

    # ------------------------------------------------------------
    # Basic helpers
    # ------------------------------------------------------------
    def label(self, text, size=28, color=WHITE_TEXT, weight=NORMAL, line_spacing=-1):
        return Text(
            text,
            font=FONT,
            font_size=size,
            color=color,
            weight=weight,
            line_spacing=line_spacing,
        )

    def section_title(self, text, color=WHITE_TEXT):
        title = self.label(text, size=30, color=color, weight=BOLD)
        title.to_edge(UP, buff=0.35)
        rule = Line(LEFT * 3.25, RIGHT * 3.25, color=color, stroke_width=2.5)
        rule.next_to(title, DOWN, buff=0.14)
        return VGroup(title, rule)

    def card(self, title, subtitle="", color=BLUE_C, width=2.35, height=1.20,
             title_size=22, sub_size=14):
        box = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.16,
            stroke_color=color,
            stroke_width=2.4,
            fill_color=color,
            fill_opacity=0.12,
        )

        title_mob = self.label(title, size=title_size, color=WHITE_TEXT, weight=BOLD)
        if title_mob.width > width - 0.32:
            title_mob.scale_to_fit_width(width - 0.32)

        if subtitle:
            sub_mob = self.label(subtitle, size=sub_size, color=MUTED)
            if sub_mob.width > width - 0.30:
                sub_mob.scale_to_fit_width(width - 0.30)
            content = VGroup(title_mob, sub_mob).arrange(DOWN, buff=0.10)
        else:
            content = VGroup(title_mob)

        content.move_to(box.get_center())
        return VGroup(box, content)

    def arrow_between(self, left, right, color=GREY_B, buff=0.14, stroke_width=4):
        return Arrow(
            left.get_right(),
            right.get_left(),
            buff=buff,
            color=color,
            stroke_width=stroke_width,
            max_tip_length_to_length_ratio=0.16,
        )

    def shield(self, color=BLUE_DP):
        outer = RegularPolygon(n=6, radius=0.68, color=color, stroke_width=3)
        outer.rotate(PI / 6)
        outer.set_fill(color, opacity=0.10)
        eps = self.label("ε-DP", size=22, color=WHITE_TEXT, weight=BOLD)
        eps.move_to(outer)
        return VGroup(outer, eps)

    # ------------------------------------------------------------
    # 1) Opening: 0.00 - 6.75
    # ------------------------------------------------------------
    def opening_title(self):
        title = self.label("7. Conclusion", size=48, color=WHITE_TEXT, weight=BOLD)
        subtitle = self.label("Complete System for DP Synthetic Data", size=26, color=BLUE_DP)
        rule = Line(LEFT * 3.8, RIGHT * 3.8, color=BLUE_DP, stroke_width=3)
        group = VGroup(title, subtitle, rule).arrange(DOWN, buff=0.24)
        group.move_to(ORIGIN)

        self.play(Write(title), run_time=1.15)
        self.play(FadeIn(subtitle, shift=UP * 0.12), Create(rule), run_time=0.95)
        self.hold_until(6.75)
        self.clean_screen()

    # ------------------------------------------------------------
    # 2) Why complete system: 6.75 - 23.50
    # ------------------------------------------------------------
    def recap_problem(self):
        title = self.section_title("Why do we need a complete system?", BLUE_DP)

        raw = self.card("Raw Data", "Text • Image • Table", ORANGE_DATA, width=2.50)
        risk = self.card("Privacy Risk", "real people may be exposed", RED_RISK, width=2.85, sub_size=13)
        synth = self.card("Synthetic Data", "useful but not copied", GREEN_SYNTH, width=2.85, sub_size=13)

        row = VGroup(raw, risk, synth).arrange(RIGHT, buff=0.50)
        row.move_to(UP * 0.42)

        arr1 = self.arrow_between(raw, risk, RED_RISK)
        arr2 = self.arrow_between(risk, synth, GREEN_SYNTH)

        question = self.label(
            "Goal: share useful data while protecting each individual.",
            size=25,
            color=WHITE_TEXT,
            weight=BOLD,
        )
        question.next_to(row, DOWN, buff=0.68)

        note = self.label(
            "DP synthetic data is not one step — it is a pipeline.",
            size=21,
            color=YELLOW_EVAL,
            weight=BOLD,
        )
        note.next_to(question, DOWN, buff=0.28)

        self.play(FadeIn(title, shift=DOWN * 0.12), run_time=0.80)
        self.play(FadeIn(raw, shift=UP * 0.12), run_time=0.90)
        self.play(Create(arr1), FadeIn(risk, shift=UP * 0.12), run_time=1.00)
        self.play(Create(arr2), FadeIn(synth, shift=UP * 0.12), run_time=1.00)
        self.play(Write(question), run_time=1.10)
        self.play(Write(note), run_time=0.95)

        self.hold_until(23.50)
        self.clean_screen()

    # ------------------------------------------------------------
    # 3) Pipeline: 23.50 - 40.00
    # ------------------------------------------------------------
    def complete_pipeline(self):
        title = self.section_title("Complete DP Synthetic Data Pipeline", WHITE_TEXT)

        raw = self.card("1. Raw Data", "sensitive records", ORANGE_DATA, width=2.15)
        bound = self.card("2. Bound", "limit each person", YELLOW_EVAL, width=2.15)
        dp = self.card("3. DP Mechanism", "controlled noise", BLUE_DP, width=2.50, title_size=19)
        gen = self.card("4. Generator", "model learns patterns", PURPLE_MODEL, width=2.30)

        synth = self.card("5. Synthetic Data", "new generated samples", GREEN_SYNTH, width=2.55, title_size=18)
        evaluate = self.card("6. Evaluate", "utility + privacy", YELLOW_EVAL, width=2.25)
        publish = self.card("7. Publish", "share safely", CYAN_PUBLISH, width=2.20)

        row1 = VGroup(raw, bound, dp, gen).arrange(RIGHT, buff=0.28)
        row1.move_to(UP * 0.78)

        row2 = VGroup(synth, evaluate, publish).arrange(RIGHT, buff=0.34)
        row2.move_to(DOWN * 1.00 + RIGHT * 0.55)

        arrows1 = VGroup(
            self.arrow_between(raw, bound),
            self.arrow_between(bound, dp),
            self.arrow_between(dp, gen),
        )
        arrows2 = VGroup(
            self.arrow_between(synth, evaluate),
            self.arrow_between(evaluate, publish),
        )

        summary = self.label(
            "Privacy is designed before the data is released.",
            size=22,
            color=BLUE_DP,
            weight=BOLD,
        )
        summary.to_edge(DOWN, buff=0.42)

        # No icons in boxes 1, 3, 5. No arrow from 4 to 5.
        self.play(FadeIn(title), run_time=0.70)
        self.play(FadeIn(raw), run_time=0.70)
        self.play(Create(arrows1[0]), FadeIn(bound), run_time=0.75)
        self.play(Create(arrows1[1]), FadeIn(dp), run_time=0.75)
        self.play(Create(arrows1[2]), FadeIn(gen), run_time=0.75)

        self.wait(0.60)

        self.play(FadeIn(synth), run_time=0.75)
        self.play(Create(arrows2[0]), FadeIn(evaluate), run_time=0.75)
        self.play(Create(arrows2[1]), FadeIn(publish), run_time=0.75)
        self.play(Write(summary), run_time=0.90)

        self.hold_until(40.00)
        self.clean_screen()

    # ------------------------------------------------------------
    # 4) Evaluation: 40.00 - 47.40
    # ------------------------------------------------------------
    def evaluation_loop(self):
        title = self.section_title("Evaluation before publishing", YELLOW_EVAL)

        fidelity = self.card("Fidelity", "similar statistics", GREEN_SYNTH, width=2.35)
        utility = self.card("Utility", "useful for ML / analysis", BLUE_DP, width=2.70, sub_size=13)
        privacy = self.card("Privacy Audit", "membership / re-ID tests", RED_RISK, width=2.95, title_size=18, sub_size=13)

        metrics = VGroup(fidelity, utility, privacy).arrange(RIGHT, buff=0.42)
        metrics.move_to(UP * 0.52)

        generator = self.card("Adjust Generator", "or privacy budget", PURPLE_MODEL, width=3.00, title_size=20)
        generator.move_to(DOWN * 1.40)

        top_y = generator.get_top()[1] + 0.02
        target_left = np.array([generator.get_center()[0] - 0.72, top_y, 0])
        target_mid = np.array([generator.get_center()[0], top_y, 0])
        target_right = np.array([generator.get_center()[0] + 0.72, top_y, 0])

        source_y = metrics.get_bottom()[1] - 0.02
        source_left = np.array([fidelity.get_center()[0], source_y, 0])
        source_mid = np.array([utility.get_center()[0], source_y, 0])
        source_right = np.array([privacy.get_center()[0], source_y, 0])

        arrow_left = Arrow(source_left, target_left, buff=0.0, color=YELLOW_EVAL, stroke_width=5,
                           max_tip_length_to_length_ratio=0.16)
        arrow_mid = Arrow(source_mid, target_mid, buff=0.0, color=YELLOW_EVAL, stroke_width=5,
                          max_tip_length_to_length_ratio=0.16)
        arrow_right = Arrow(source_right, target_right, buff=0.0, color=YELLOW_EVAL, stroke_width=5,
                            max_tip_length_to_length_ratio=0.16)

        note = self.label(
            "If one metric fails, we tune again before publishing.",
            size=22,
            color=YELLOW_EVAL,
            weight=BOLD,
        )
        note.to_edge(DOWN, buff=0.40)

        self.play(FadeIn(title), run_time=0.65)
        self.play(LaggedStart(*[FadeIn(m, shift=UP * 0.10) for m in metrics], lag_ratio=0.12), run_time=1.00)
        self.play(FadeIn(generator, shift=UP * 0.10), run_time=0.65)
        self.play(Create(arrow_left), Create(arrow_mid), Create(arrow_right), run_time=0.85)
        self.play(Write(note), run_time=0.70)

        self.hold_until(47.40)
        self.clean_screen()

    # ------------------------------------------------------------
    # 5) When to use: 47.40 - 62.20
    # ------------------------------------------------------------
    def when_to_use(self):
        title = self.section_title("When should we use DP synthetic data?", WHITE_TEXT)

        left_box = RoundedRectangle(width=5.90, height=3.10, corner_radius=0.18,
                                    color=GREEN_SYNTH, stroke_width=2.5)
        left_box.set_fill(GREEN_SYNTH, opacity=0.07)
        right_box = RoundedRectangle(width=5.55, height=3.10, corner_radius=0.18,
                                     color=RED_RISK, stroke_width=2.5)
        right_box.set_fill(RED_RISK, opacity=0.07)

        good_items = VGroup(
            self.label("Use it when:", size=24, color=GREEN_SYNTH, weight=BOLD),
            self.label("• data is sensitive", size=18),
            self.label("• sharing is needed", size=18),
            self.label("• trends matter more than exact rows", size=18),
            self.label("• a formal privacy guarantee is required", size=17),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.17)

        careful_items = VGroup(
            self.label("Be careful when:", size=24, color=RED_RISK, weight=BOLD),
            self.label("• the dataset is very small", size=18),
            self.label("• exact original records are required", size=18),
            self.label("• the privacy budget is too loose", size=18),
            self.label("• no audit is performed", size=18),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.17)

        left_group = VGroup(left_box, good_items)
        right_group = VGroup(right_box, careful_items)
        board = VGroup(left_group, right_group).arrange(RIGHT, buff=0.48)
        board.move_to(DOWN * 0.18)

        good_items.move_to(left_box.get_center()).align_to(left_box.get_left() + RIGHT * 0.34, LEFT)
        careful_items.move_to(right_box.get_center()).align_to(right_box.get_left() + RIGHT * 0.34, LEFT)

        self.play(FadeIn(title), run_time=0.70)
        self.play(FadeIn(left_box), LaggedStart(*[Write(x) for x in good_items], lag_ratio=0.10), run_time=1.30)
        self.play(FadeIn(right_box), LaggedStart(*[Write(x) for x in careful_items], lag_ratio=0.10), run_time=1.30)

        self.hold_until(62.20)
        self.clean_screen()

    # ------------------------------------------------------------
    # 6) Tradeoff: 62.20 - 72.40
    # ------------------------------------------------------------
    def privacy_utility_tradeoff(self):
        title = self.section_title("Main lesson: balance privacy and utility", BLUE_DP)

        beam = Line(LEFT * 3.25, RIGHT * 3.25, color=WHITE_TEXT, stroke_width=5)
        fulcrum = Triangle(color=GREY_B, fill_color=GREY_B, fill_opacity=0.50).scale(0.36).rotate(PI)
        beam.move_to(UP * 0.00)
        fulcrum.next_to(beam, DOWN, buff=0.12)

        privacy_weight = Circle(radius=0.44, color=BLUE_DP, fill_color=BLUE_DP, fill_opacity=0.18)
        privacy_icon = self.label("ε", size=33, color=WHITE_TEXT, weight=BOLD).move_to(privacy_weight)
        privacy = VGroup(privacy_weight, privacy_icon).move_to(LEFT * 2.20 + UP * 0.05)
        privacy_label = self.label("Privacy", size=24, color=BLUE_DP, weight=BOLD).next_to(privacy, UP, buff=0.14)

        utility_weight = Circle(radius=0.44, color=GREEN_SYNTH, fill_color=GREEN_SYNTH, fill_opacity=0.18)
        utility_icon = self.label("ML", size=22, color=WHITE_TEXT, weight=BOLD).move_to(utility_weight)
        utility = VGroup(utility_weight, utility_icon).move_to(RIGHT * 2.20 + UP * 0.05)
        utility_label = self.label("Utility", size=24, color=GREEN_SYNTH, weight=BOLD).next_to(utility, UP, buff=0.14)

        notes = VGroup(
            self.label("More privacy  →  stronger protection, but less detail.", size=21, color=BLUE_DP),
            self.label("More utility  →  better analysis, but privacy must be audited.", size=21, color=GREEN_SYNTH),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        notes.next_to(beam, DOWN, buff=0.95)

        self.play(FadeIn(title), run_time=0.70)
        self.play(Create(beam), FadeIn(fulcrum), FadeIn(privacy), FadeIn(utility),
                  Write(privacy_label), Write(utility_label), run_time=1.15)
        self.play(Rotate(beam, angle=0.07, about_point=fulcrum.get_top()), run_time=0.70)
        self.play(Rotate(beam, angle=-0.14, about_point=fulcrum.get_top()), run_time=0.75)
        self.play(Rotate(beam, angle=0.07, about_point=fulcrum.get_top()), run_time=0.70)
        self.play(LaggedStart(*[Write(n) for n in notes], lag_ratio=0.16), run_time=0.95)

        self.hold_until(72.40)
        self.clean_screen()

    # ------------------------------------------------------------
    # 7) Final: 72.40 - 81.685
    # ------------------------------------------------------------
    def final_message(self):
        raw = self.card("Private Data", "people stay protected", ORANGE_DATA, width=2.55)
        dp = self.shield().scale(0.90)
        synth = self.card("Synthetic Data", "research moves forward", GREEN_SYNTH, width=2.70)

        final_pipeline = VGroup(raw, dp, synth).arrange(RIGHT, buff=0.80)
        final_pipeline.move_to(UP * 0.72)
        arrows = VGroup(
            self.arrow_between(raw, dp, BLUE_DP, buff=0.16),
            self.arrow_between(dp, synth, GREEN_SYNTH, buff=0.16),
        )

        message = self.label("Protect Privacy, Unlock Data", size=40, color=WHITE_TEXT, weight=BOLD)
        glow = SurroundingRectangle(message, buff=0.24, color=BLUE_DP, corner_radius=0.18)
        glow.set_fill(BLUE_DP, opacity=0.07)
        message_group = VGroup(glow, message).next_to(final_pipeline, DOWN, buff=0.72)

        subtitle = self.label(
            "DP synthetic data is a controlled release system.",
            size=22,
            color=MUTED,
            weight=BOLD,
        )
        subtitle.next_to(message_group, DOWN, buff=0.30)

        self.play(FadeIn(raw, shift=RIGHT * 0.10), run_time=0.70)
        self.play(Create(arrows[0]), FadeIn(dp, scale=0.85), run_time=0.70)
        self.play(Create(arrows[1]), FadeIn(synth, shift=RIGHT * 0.10), run_time=0.70)
        self.play(Create(glow), Write(message), run_time=1.00)
        self.play(FadeIn(subtitle, shift=UP * 0.05), run_time=0.60)

        self.hold_until(self.AUDIO_DURATION)

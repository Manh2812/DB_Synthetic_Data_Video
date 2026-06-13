from manim import *
import numpy as np

# Define colors
CYAN = "#00FFFF"
PINK = "#FF00FF"
GREEN = "#00FF00"
RED = "#FF0000"
YELLOW = "#FFFF00"
WHITE = "#FFFFFF"
LIGHT_GRAY = "#CCCCCC"
FONT = "DejaVu Sans"
MAX_TEXT_WIDTH = 11.2


def fit_width(mobject, max_width=MAX_TEXT_WIDTH):
    if mobject.width > max_width:
        mobject.scale_to_fit_width(max_width)
    return mobject


def vi_text(text, font_size=30, color=WHITE, max_width=MAX_TEXT_WIDTH):
    return fit_width(Text(text, font_size=font_size, font=FONT, color=color), max_width)


class Scene2DP(Scene):
    def construct(self):
        # Set background color to black
        self.camera.background_color = "#000000"
        
        # ============ PART 1: TITLE & INTRODUCTION ============
        title = vi_text("Differential Privacy (DP)", font_size=56)
        subtitle = vi_text("Quyền riêng tư vi sai trong phân tích học máy",
                           font_size=28, color=LIGHT_GRAY)
        subtitle.next_to(title, DOWN, buff=0.6)
        
        self.play(Write(title, run_time=2))
        self.wait(1)
        self.play(Write(subtitle, run_time=2))
        self.wait(5)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=1.5)
        self.wait(1)
        
        # ============ PART 2: NEIGHBORING DATASETS ============
        part2_title = vi_text("Neighboring Datasets: D1 và D2", font_size=42)
        part2_title.to_edge(UP)
        self.play(Write(part2_title, run_time=2))
        self.wait(1.5)
        
        # Create two datasets
        dataset_title = vi_text("Hai tập dữ liệu chỉ khác đúng 1 người",
                                font_size=30, color=YELLOW)
        dataset_title.next_to(part2_title, DOWN, buff=0.35)
        self.play(Write(dataset_title, run_time=2))
        self.wait(2.5)
        
        # Dataset D1
        d1_title = MathTex(r"D_1", font_size=48, color=WHITE)
        d1_items = VGroup(
            vi_text("Alice (30 tuổi)", font_size=24, max_width=3.5),
            vi_text("Bob (45 tuổi)", font_size=24, max_width=3.5),
            vi_text("Charlie (35 tuổi)", font_size=24, max_width=3.5),
        )
        d1_items.arrange(DOWN, buff=0.4)
        d1_box = SurroundingRectangle(d1_items, buff=0.35, stroke_color=CYAN, stroke_width=2)
        d1 = VGroup(d1_title, d1_box, d1_items)
        VGroup(d1_title, VGroup(d1_box, d1_items)).arrange(DOWN, buff=0.35)
        d1.to_edge(LEFT, buff=1)
        
        # Dataset D2 (same but Charlie is replaced)
        d2_title = MathTex(r"D_2", font_size=48, color=WHITE)
        d2_items = VGroup(
            vi_text("Alice (30 tuổi)", font_size=24, max_width=3.5),
            vi_text("Bob (45 tuổi)", font_size=24, max_width=3.5),
            vi_text("Diana (28 tuổi)", font_size=24, color=RED, max_width=3.5),
        )
        d2_items.arrange(DOWN, buff=0.4)
        d2_box = SurroundingRectangle(d2_items, buff=0.35, stroke_color=PINK, stroke_width=2)
        d2 = VGroup(d2_title, d2_box, d2_items)
        VGroup(d2_title, VGroup(d2_box, d2_items)).arrange(DOWN, buff=0.35)
        d2.to_edge(RIGHT, buff=1)
        
        self.play(Create(d1_box), Write(d1_title), Write(d1_items), run_time=3)
        self.wait(2)
        self.play(Create(d2_box), Write(d2_title), Write(d2_items), run_time=3)
        self.wait(3)
        
        # Highlight difference
        diff_note = vi_text("Khác biệt chính xác một điểm dữ liệu",
                            font_size=28, color=GREEN)
        diff_note.to_edge(DOWN, buff=1)
        self.play(Write(diff_note, run_time=2))
        self.wait(4)
        
        # Cleanup
        self.play(
            FadeOut(part2_title), FadeOut(dataset_title), 
            FadeOut(d1_box), FadeOut(d1_title), FadeOut(d1_items),
            FadeOut(d2_box), FadeOut(d2_title), FadeOut(d2_items), 
            FadeOut(diff_note), run_time=1.5
        )
        self.wait(1)
        
        # ============ PART 3: ALGORITHM & QUERY ============
        algo_title = vi_text("Chạy cùng thuật toán M trên hai tập dữ liệu",
                             font_size=38)
        algo_title.to_edge(UP)
        self.play(Write(algo_title, run_time=2))
        self.wait(1.5)
        
        # Simple query: Average Age
        query = vi_text("Truy vấn: Tính độ tuổi trung bình",
                        font_size=30, color=YELLOW)
        query.next_to(algo_title, DOWN, buff=0.5)
        self.play(Write(query, run_time=2))
        self.wait(2)
        
        # Show calculation for D1
        d1_calc = VGroup(
            MathTex(r"D_1:", font_size=36, color=WHITE),
            vi_text("(30 + 45 + 35) / 3 = 36.67", font_size=28, max_width=4.6),
        )
        d1_calc.arrange(DOWN, buff=0.4)
        d1_calc.to_edge(LEFT, buff=1)
        
        # Show calculation for D2
        d2_calc = VGroup(
            MathTex(r"D_2:", font_size=36, color=WHITE),
            vi_text("(30 + 45 + 28) / 3 = 34.33", font_size=28, max_width=4.6),
        )
        d2_calc.arrange(DOWN, buff=0.4)
        d2_calc.to_edge(RIGHT, buff=1)
        
        self.play(Write(d1_calc, run_time=3))
        self.wait(2)
        self.play(Write(d2_calc, run_time=3))
        self.wait(3)
        
        # Show results
        result1 = vi_text("Kết quả: 36.67", font_size=30, color=CYAN, max_width=4.4)
        result1.next_to(d1_calc, DOWN, buff=1.5)
        
        result2 = vi_text("Kết quả: 34.33", font_size=30, color=PINK, max_width=4.4)
        result2.next_to(d2_calc, DOWN, buff=1.5)
        
        self.play(Write(result1, run_time=2), Write(result2, run_time=2))
        self.wait(3)
        
        # Show problem: Can tell difference
        problem = vi_text("Kết quả khác nhau có thể làm lộ thông tin!",
                          font_size=30, color=RED)
        problem.to_edge(DOWN, buff=1)
        self.play(Write(problem, run_time=2))
        self.wait(5)
        
        self.play(
            FadeOut(algo_title), FadeOut(query), FadeOut(d1_calc), 
            FadeOut(d2_calc), FadeOut(result1), FadeOut(result2), 
            FadeOut(problem), run_time=1.5
        )
        self.wait(1)
        
        # ============ PART 4: ADDING NOISE ============
        noise_title = vi_text("Giải pháp: Thêm nhiễu Laplace", font_size=40)
        noise_title.to_edge(UP)
        self.play(Write(noise_title, run_time=2))
        self.wait(1.5)
        
        # Laplace mechanism formula
        laplace_formula = MathTex(r"\mathcal{M}(D) = f(D) + \text{Laplace}\left(0, \frac{\Delta f}{\epsilon}\right)", font_size=40, color=WHITE)
        fit_width(laplace_formula, 10.6)
        laplace_formula.next_to(noise_title, DOWN, buff=0.6)
        self.play(Write(laplace_formula, run_time=3))
        self.wait(3)
        
        # Explanation of parameters
        explanation = VGroup(
            vi_text("f(D): Kết quả truy vấn gốc", font_size=27, max_width=9.8),
            vi_text("Δf: Độ nhạy - mức thay đổi tối đa do một cá nhân gây ra",
                    font_size=27, max_width=9.8),
            vi_text("ε: Tham số riêng tư - epsilon nhỏ tạo nhiều nhiễu hơn",
                    font_size=27, max_width=9.8),
        )
        explanation.arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        explanation.next_to(laplace_formula, DOWN, buff=0.65)
        
        self.play(Write(explanation, run_time=4))
        self.wait(5)
        
        self.play(FadeOut(explanation), run_time=1.5)
        
        # Show noisy results
        noisy_title = vi_text("Sau khi thêm nhiễu Laplace:",
                              font_size=30, color=LIGHT_GRAY)
        noisy_title.next_to(laplace_formula, DOWN, buff=0.8)
        
        # Simulate noisy results
        np.random.seed(42)
        noisy1 = 36.67 + np.random.laplace(0, 2.34/0.5)
        noisy2 = 34.33 + np.random.laplace(0, 2.34/0.5)
        
        noisy_result1 = MathTex(rf"\mathcal{{M}}(D_1) = {noisy1:.2f}", font_size=40, color=WHITE)
        noisy_result1.next_to(noisy_title, DOWN, buff=0.5)
        
        noisy_result2 = MathTex(rf"\mathcal{{M}}(D_2) = {noisy2:.2f}", font_size=40, color=WHITE)
        noisy_result2.next_to(noisy_result1, DOWN, buff=0.4)
        
        self.play(Write(noisy_title, run_time=2))
        self.wait(1.5)
        self.play(Write(noisy_result1, run_time=2))
        self.wait(1.5)
        self.play(Write(noisy_result2, run_time=2))
        self.wait(3)
        
        # Highlight similarity
        similar = vi_text("Kết quả dao động gần nhau: khó phân biệt D1 và D2",
                          font_size=27, color=GREEN)
        similar.to_edge(DOWN, buff=1)
        self.play(Write(similar, run_time=2))
        self.wait(5)
        
        self.play(
            FadeOut(noise_title), FadeOut(laplace_formula), 
            FadeOut(noisy_title), FadeOut(noisy_result1), 
            FadeOut(noisy_result2), FadeOut(similar), run_time=1.5
        )
        self.wait(1)
        
        # ============ PART 5: EPSILON-DP DEFINITION ============
        dp_def_title = vi_text("Định nghĩa Differential Privacy", font_size=40)
        dp_def_title.to_edge(UP)
        self.play(Write(dp_def_title, run_time=2))
        self.wait(1.5)
        
        # Mathematical definition
        dp_formula = vi_text("Thuật toán M thỏa mãn ε-DP nếu với mọi",
                             font_size=26, max_width=10.4)
        dp_formula2 = vi_text("tập láng giềng D1, D2 và mọi tập đầu ra S:",
                              font_size=26, max_width=10.4)
        dp_formula.next_to(dp_def_title, DOWN, buff=0.55)
        dp_formula2.next_to(dp_formula, DOWN, buff=0.22)
        
        self.play(Write(dp_formula, run_time=2), Write(dp_formula2, run_time=2))
        self.wait(3)
        
        # The actual formula MUST be LaTeX and white
        main_formula = MathTex(
            r"\mathbb{P}[\mathcal{M}(D_1) \in S]"
            r"\le e^\epsilon \cdot"
            r"\mathbb{P}[\mathcal{M}(D_2) \in S]",
            font_size=42,
            color=WHITE,
        )
        fit_width(main_formula, 10.4)
        main_formula.next_to(dp_formula2, DOWN, buff=0.75)
        self.play(Write(main_formula, run_time=4))
        self.wait(4)
        
        # Explanation
        explanation2 = VGroup(
            vi_text("• Tỉ lệ xác suất đầu ra bị chặn bởi e mũ epsilon",
                    font_size=23, max_width=10.4),
            vi_text("• Cá nhân được an toàn và khó bị phân biệt",
                    font_size=23, max_width=10.4),
            vi_text("• Dữ liệu của một người không được chi phối phân tích!",
                    font_size=24, color=GREEN, max_width=10.4),
        )
        explanation2.arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        explanation2.next_to(main_formula, DOWN, buff=0.9)
        if explanation2.get_bottom()[1] < -3.15:
            explanation2.to_edge(DOWN, buff=0.45)
        
        self.play(Write(explanation2, run_time=4))
        self.wait(6)
        
        self.play(
            FadeOut(dp_def_title), FadeOut(dp_formula), FadeOut(dp_formula2), 
            FadeOut(main_formula), FadeOut(explanation2), run_time=1.5
        )
        self.wait(1)
        
        # ============ PART 6: PRIVACY BUDGET ============
        budget_title = vi_text("Ngân sách quyền riêng tư (ε)", font_size=40)
        budget_title.to_edge(UP)
        self.play(Write(budget_title, run_time=2))
        self.wait(1.5)
        
        budget_explain = VGroup(
            vi_text("ε nhỏ: riêng tư cao hơn, nhiễu nhiều hơn",
                    font_size=27, color=GREEN, max_width=10.4),
            vi_text("ε lớn: hữu dụng cao hơn, rủi ro lộ thông tin tăng",
                    font_size=27, color=RED, max_width=10.4),
        )
        budget_explain.arrange(DOWN, buff=0.65)
        budget_explain.next_to(budget_title, DOWN, buff=0.9)
        
        self.play(Write(budget_explain, run_time=4))
        self.wait(4)
        
        # Budget visualization
        budget_scale = Line(
            start=np.array([-5, -1.5, 0]),
            end=np.array([5, -1.5, 0]),
            color=WHITE,
            stroke_width=3
        )
        
        # Add epsilon values on scale
        epsilon_points = VGroup()
        for i, eps in enumerate([0.1, 0.5, 1.0, 5.0, 10.0]):
            x = -5 + i * 2.5
            point = Dot(np.array([x, -1.5, 0]), color=WHITE, radius=0.1)
            label = MathTex(rf"\epsilon={eps}", font_size=28, color=WHITE)
            label.next_to(point, DOWN, buff=0.4)
            epsilon_points.add(point)
            epsilon_points.add(label)
        
        self.play(Create(budget_scale, run_time=2))
        self.play(Write(epsilon_points, run_time=4))
        self.wait(4)
        
        # Show privacy-utility trade-off
        tradeoff = vi_text("Đánh đổi giữa riêng tư và tính hữu dụng",
                           font_size=30, color=LIGHT_GRAY)
        tradeoff.to_edge(DOWN, buff=1)
        self.play(Write(tradeoff, run_time=3))
        self.wait(5)
        
        self.play(
            FadeOut(budget_title), FadeOut(budget_explain), 
            FadeOut(budget_scale), FadeOut(epsilon_points), FadeOut(tradeoff), run_time=1.5
        )
        self.wait(1)
        
        # ============ PART 7: CONCLUSION ============
        conclusion_title = vi_text("Điểm mấu chốt", font_size=50)
        conclusion_title.to_edge(UP)
        self.play(Write(conclusion_title, run_time=2))
        self.wait(2)
        
        conclusion = VGroup(
            vi_text("Dữ liệu của một cá nhân", font_size=40, color=YELLOW),
            vi_text("không được chi phối phân tích", font_size=40, color=YELLOW),
        )
        conclusion.arrange(DOWN, buff=0.4)
        conclusion.move_to(ORIGIN)
        
        self.play(Write(conclusion, run_time=4))
        self.wait(5)
        
        # Final message
        final_msg = vi_text("Differential Privacy là bảo chứng toán học cho điều đó",
                            font_size=30, color=LIGHT_GRAY)
        final_msg.to_edge(DOWN, buff=1.5)
        self.play(Write(final_msg, run_time=3))
        self.wait(7)
        
        self.play(
            FadeOut(conclusion_title), FadeOut(conclusion), FadeOut(final_msg), run_time=2
        )

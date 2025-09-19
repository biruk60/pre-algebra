
from manim import * 
import manimpango

class TableOfContents(Scene):
    def construct(self):
        # Register custom font if available
        manimpango.register_font("assets/fonts/Nyala Regular.ttf")
        self.wait()
        
        # Modified sections with indentation for "Propositions" under "Proposition"
        sections = [
            "0. Introduction",
            "1. Proposition",
            "    1.1 Proposition Types",  # Indented to show hierarchy
            "    1.2 Propositional Connectives",  # Indented to show hierarchy
            "       1.2.1 Negation",  # Indented to show hierarchy
            "Background",
            "Methods",
            "Results",
            "Discussion",
            "Conclusion"
        ]
        
        # Create MarkupText for each section
        section_texts = []
        for section in sections:
            # Count leading spaces for indentation simulation
            leading_spaces = len(section) - len(section.lstrip(' '))
            indent_shift = leading_spaces * 0.3  # tweak this for horizontal indent size
            text = MarkupText(section.strip(), font_size=36, font="Nyala")
            text.shift(indent_shift * LEFT)  # shift left or right based on indent
            section_texts.append(text)
        
        # Arrange vertically with spacing but ignoring horizontal alignment to keep indentation
        toc = VGroup(*section_texts).arrange(DOWN, buff=0.7)
        
        # Create highlights
        highlights = VGroup(*[
            Rectangle(
                width=text.width + 0.5,
                height=text.height + 0.2,
                fill_opacity=0,
                fill_color=YELLOW,
                stroke_width=0
            ).move_to(text)
            for text in section_texts
        ])
        
        # Group highlights and text side by side
        grouped = VGroup(*[
            VGroup(rect, text) for rect, text in zip(highlights, section_texts)
        ]).arrange(DOWN, buff=0.7)

        self.add(grouped)
        
        # Animate highlight for each line sequentially
        for i in range(len(section_texts)):
            self.play(highlights[i].animate.set_fill(YELLOW, opacity=0.5), run_time=1)
            self.wait(1)
            if i < len(section_texts) - 1:
                self.play(highlights[i].animate.set_fill(YELLOW, opacity=0), run_time=0.5)

        self.wait(2)

 class SetColumnColorsExample(Scene):
    def construct(self):
        table = Table(
            [["T", "F"],
            ["F","T"]],
            # row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("P"), Text("~P")]
        ).set_column_colors([BLUE], [GREEN],[YELLOW])
        # table = Table(
        #      [["", ""],
        #      ["", ""]],
        #     col_labels=[Text("P"), Text("~P")]
        # ).set_column_colors([BLUE], [GREEN],[YELLOW])
        # table.get_cell((1, 1)).add(Text("T"))
        # table.get_cell((1, 2)).add(Text("F"))
        # table.get_cell((2, 1)).add(Text("F"))
        # table.get_cell((2, 2)).add(Text("T"))
        col1 = SurroundingRectangle(table.get_columns()[0])
        col2 = SurroundingRectangle(table.get_columns()[1])
        row1 = SurroundingRectangle(table.get_rows()[1])
        row2 = SurroundingRectangle(table.get_rows()[2])
        cell1 = SurroundingRectangle(table.get_cell((1,1)), color=RED)
        cell1_content = SurroundingRectangle(table.get_entries((2, 1)), color=BLUE)
        cell2_content = SurroundingRectangle(table.get_entries((3, 1)), color=BLUE)
        self.play(Create(table), run_time=1)
        self.wait() 
        # self.play(chama.animate.set_opacity(1), run_time=1)
        self.play(Create(col1), run_time=1)
        self.wait() 
        # highlight = table.get_cells((2,1), color=GREEN, fill_opacity=.75)
        # table.add_to_back(highlight)
        self.play(Create(cell1), run_time=1)
        self.wait() 
        self.play(Create(cell1_content), run_time=1)
        self.wait()
        self.play(ReplacementTransform(cell1_content, cell2_content), run_time=1)
        self.wait()
        self.play(FadeOut(cell2_content), ReplacementTransform(col1, col2), run_time=1)
        self.wait()
        # self.play(ReplacementTransform(col1, col2), run_time=1)
        # self.wait()
        self.play(FadeOut(col2), run_time=1)
        self.wait()
        self.play(Create(row1), run_time=1)
        self.wait()
        self.play(ReplacementTransform(row1, row2), run_time=1)
        self.wait()
        
       
class TruthTableNEGATION(Scene):
    def construct(self):
        # Table content
        headers = ["p", "¬ p"]
        table_data = [
            ["T", "F"],
            ["F", "T"],            
        ]

        # Create table object without MathTex
        table = Table(
            table_data,
            col_labels=[Text(h) for h in headers],  # Use Text here
            include_outer_lines=False,
        )            
        table.center()
        # Get each column as a VGroup
        first_col = VGroup(table.get_columns()[0], table.get_col_labels()[0])
        second_col = VGroup(table.get_columns()[1], table.get_col_labels()[1])
        # Add to scene
        
        # Hide all columns initially
        for col in [first_col, second_col]:
            col.set_opacity(0)
        
        self.add(table)
        self.play(first_col[1].animate.set_opacity(1))
        self.wait(0.3)
        self.play(second_col[1].animate.set_opacity(1))
        self.wait(0.3)
    
        for cell in first_col[0]:
            self.play(cell.animate.set_opacity(1))
            self.wait(0.3)
            
        self.wait(1)
        
        for cell in second_col[0]:
            self.play(cell.animate.set_opacity(1))
            self.wait(0.3)
            
        self.wait(2) 
        self.play(table.animate.set_opacity(0)) 
        self.wait(2)  
        

# manim -ql -p --disable_caching  -o outro_video.mp4 .\outro.py OutroScene

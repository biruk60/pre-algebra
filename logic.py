
from manim import * 
import manimpango

class TableOfContents(Scene):
    def construct(self):
        background = ImageMobject("assets/images/blackboard.png")
        
        # Scale the image to fit the height of the scene (approx 8 units)
        background.scale_to_fit_height(config.frame_height)
        
        # Move it to the center and push it back behind other mobjects
        background.move_to(ORIGIN).set_z_index(-1)
        
        # Add background
        self.add(background)
        manimpango.register_font("assets/fonts/Nyala Regular.ttf")
        self.wait()
        font_size = 25
        intro = MarkupText("- መእተዊ", font_size=font_size, font="Nyala")
        proposition = MarkupText("- ሓሳብ", font_size=font_size, font="Nyala", color='#FFFFF0')
        prop_types = MarkupText("- ዓይነታት", font_size=font_size, font="Nyala")
        prop_connectives = MarkupText("- መጣመርቲ", font_size=font_size, font="Nyala")
        negation = MarkupText("- ኣሉታ", font_size=font_size, font="Nyala")
        disjunction = MarkupText("- ፍልያ", font_size=font_size, font="Nyala")
        conjunction = MarkupText("- መስተጻምር", font_size=font_size, font="Nyala")
        implication = MarkupText("- ኣገዳስነት", font_size=font_size, font="Nyala")
        biimplication = MarkupText("- ክልተ-ኣገዳስነት", font_size=font_size, font="Nyala")
        converse = MarkupText("- ኣንጻር፣ ተገላባጢ፣ ተጻራሪ ኣወንታዊ", font_size=font_size, font="Nyala",color='#FFFFF0')
        tautology = MarkupText("- ህውላለን ግርጭትን", font_size=font_size, font="Nyala", color='#FFFFF0')
        logical_equiv = MarkupText("- መጎታዊ ማዕርነት", font_size=font_size, font="Nyala", color='#FFFFF0')

        intro.move_to(ORIGIN + UP*3.1 + LEFT*4)
        proposition.next_to(intro, DOWN, buff=0.3).align_to(intro, LEFT)
        prop_types.next_to(proposition, DOWN, buff=0.3).shift(RIGHT*0.8)
        prop_connectives.next_to(prop_types, DOWN, buff=0.3).align_to(prop_types, LEFT)
        negation.next_to(prop_connectives, DOWN, buff=0.3).shift(RIGHT*0.8)
        disjunction.next_to(negation, DOWN, buff=0.3).align_to(negation, LEFT)
        conjunction.next_to(disjunction, DOWN, buff=0.3).align_to(negation, LEFT)
        implication.next_to(conjunction, DOWN, buff=0.3).align_to(negation, LEFT)
        biimplication.next_to(implication, DOWN, buff=0.3).align_to(negation, LEFT)
        converse.next_to(biimplication, DOWN, buff=0.3).align_to(negation, LEFT)
        tautology.next_to(converse, DOWN, buff=0.3).align_to(intro, LEFT)
        logical_equiv.next_to(tautology, DOWN, buff=0.3).align_to(intro, LEFT)

        toc_group = VGroup(
            intro, proposition,
            prop_types, prop_connectives,
            negation, disjunction, conjunction,
            implication, biimplication, converse,
            tautology, logical_equiv
        )
        self.add(toc_group)
        self.wait(2)
        #  sections = [
        #     (0, "Introduction"),
        #     (0, "Proposition"),
        #     (1, "Proposition Types"),
        #     (1, "Propositional Connectives"),
        #     (2, "Negation"),
        #     (2, "Disjunction"),
        #     (2, "Conjunction"),
        #     (2, "Implication"),
        #     (2, "Bi-Implication"),
        #     (2, "Converse, Inverse, and Contra Positive"),
        #     (0, "Tautology and Contradiction"),
        #     (0, "Logical Equivalence")         
           
        # ]

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

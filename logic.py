
from manim import * 
import manimpango


def layout()->[mobject.types.image_mobject.ImageMobject, mobject.text.text_mobject.Text]:
    background = ImageMobject("assets/images/blackboard.png").set_opacity(.8)
    manimpango.register_font("assets/fonts/nyala_regular.ttf")
    background.scale_to_fit_width(config.frame_width)
    background.scale_to_fit_height(config.frame_height)
    background.set_z_index(-10)  # Keep behind everything
    bg_text = Text("@BK_BROOK", fill_opacity=0.025).scale(3)
    bg_text.set_z_index(-9)  # Keep behind everything
    return background, bg_text 
        
    

class TableOfContents(Scene):
    def construct(self):
        background, bg_text = layout()
        self.add(background)   

        # Add text as a fixed background element
        self.add(bg_text)
        self.wait()
        font_size = 23
        buff=0.275       
        title = MarkupText("ትሕዝቶታት ናይ'ዚ ቪድዮ \n",font="Nyala", font_size=45).to_edge(UP) 
        intro = MarkupText("1 መእተዊ", font_size=font_size, font="Nyala")
        proposition = MarkupText("2 ሓሳብ", font_size=font_size, font="Nyala")
        prop_types = MarkupText("2.1 ዓይነታት", font_size=font_size, font="Nyala")
        prop_connectives = MarkupText("2.2 መጣመርቲ", font_size=font_size, font="Nyala")
        negation = MarkupText("2.2.1 ኣሉታ", font_size=font_size, font="Nyala")
        disjunction = MarkupText("2.2.2 ፍልያ", font_size=font_size, font="Nyala")
        conjunction = MarkupText("2.2.3 መስተጻምር", font_size=font_size, font="Nyala")
        implication = MarkupText("2.2.4 ኣገዳስነት", font_size=font_size, font="Nyala")
        biimplication = MarkupText("2.2.5 ክልተ-ኣገዳስነት", font_size=font_size, font="Nyala")
        converse = MarkupText("2.2.6 ኣንጻር፣ ተገላባጢ፣ ተጻራሪ ኣወንታዊ", font_size=font_size, font="Nyala")
        tautology = MarkupText("3 ህውላለን ግርጭትን", font_size=font_size, font="Nyala")
        logical_equiv = MarkupText("4 መጎታዊ ማዕርነት", font_size=font_size, font="Nyala")

        intro.move_to(ORIGIN + UP*2 + LEFT*4)
        proposition.next_to(intro, DOWN, buff=buff).align_to(intro, LEFT)
        prop_types.next_to(proposition, DOWN, buff=buff).shift(RIGHT*0.8)
        prop_connectives.next_to(prop_types, DOWN, buff=buff).align_to(prop_types, LEFT)
        negation.next_to(prop_connectives, DOWN, buff=buff).shift(RIGHT*0.8)
        disjunction.next_to(negation, DOWN, buff=buff).align_to(negation, LEFT)
        conjunction.next_to(disjunction, DOWN, buff=buff).align_to(negation, LEFT)
        implication.next_to(conjunction, DOWN, buff=buff).align_to(negation, LEFT)
        biimplication.next_to(implication, DOWN, buff=buff).align_to(negation, LEFT)
        converse.next_to(biimplication, DOWN, buff=buff).align_to(negation, LEFT)
        tautology.next_to(converse, DOWN, buff=buff).align_to(intro, LEFT)
        logical_equiv.next_to(tautology, DOWN, buff=buff).align_to(intro, LEFT)

        toc_group = VGroup(
            intro, proposition,
            prop_types, prop_connectives,
            negation, disjunction, conjunction,
            implication, biimplication, converse,
            tautology, logical_equiv
        )
        self.play(Write(title), run_time=.5)
        line = Line(5*LEFT, 5*RIGHT, color=[YELLOW, BLUE]).next_to(title, DOWN,buff=buff)
        self.play(Create(line))
        self.play(Write(toc_group), run_time=4)
        self.wait(4)
        for element in toc_group:
            shade = SurroundingRectangle(element, color=YELLOW, buff=.15)
            self.add(shade)
            self.bring_to_front(element)
            self.wait(0.5)
            self.remove(shade)
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
        
"""
Axiom and Axiomatic system.
********************************
An axiom in mathematics is a statement assumed to be true without proof, serving as a foundational building block for further reasoning and deduction. An axiomatic system is a structured framework consisting of a set of axioms from which mathematicians can derive theorems using logical reasoning. 

Key Properties of Axiomatic Systems
Consistency: The system does not lead to contradictions; no statement and its opposite can both be deduced.

Independence: Every axiom cannot be proven from the others; each adds unique information.

Completeness: Every statement expressible in the system can be proven true or false within it (though Gödel’s incompleteness theorem shows that some systems cannot be complete).

Famous examples include Euclid’s Elements (geometry), Peano axioms (arithmetic), Zermelo-Fraenkel axioms (set theory), and Kolmogorov’s probability axioms.


Abstraction 
************
Abstraction is the process of distilling complex ideas into simpler, more general concepts by focusing on essential properties and removing unnecessary details. In mathematics and logic, it involves extracting underlying structures, patterns, or properties of concepts, independent of specific contexts or physical examples, allowing these ideas to be generalized and applied broadly to different cases .

In logic and mathematics, abstraction is useful because it enables:

Identification of common patterns across diverse specific instances.

Creation of general theories and models applicable in many situations.

Simplification of complex problems by focusing on core properties rather than incidental details.

Enhanced logical reasoning by concentrating on essential relationships and properties.

Flexibility to work with symbolic representations that stand for whole classes of objects or concepts rather than individual cases .

Thus, abstraction is foundational for axiomatic systems since it allows mathematics to move beyond empirical notions and base itself on formal logical structures that define objects & truths from first principles


Logic: Its Etymology and History 
**********************************
Its history traces back to ancient civilizations, with notable early developments in India, China, and Greece. The discipline became systematic in ancient Greece, especially through Aristotle's work in the 4th century BCE, who is regarded as the first formal logician. Aristotle developed the theory of syllogism and laid the foundations of what is called Aristotelian or term logic.

History of Logic
Ancient logic began with Aristotle, who constructed a system of syllogistic reasoning based on categorical terms and propositions, as documented in his works called the Organon.

Medieval philosophers extended Aristotle’s work but mostly kept the traditional term logic framework.

In the 19th century, figures like George Boole, Gottlob Frege, and Bertrand Russell pioneered symbolic logic, transforming logic into a rigorous mathematical discipline.

This modern symbolic logic focuses on propositional and predicate calculus, involving symbols for logical connectives and quantifiers, emphasizing form and formal proof.
"""  

class Introduction(Scene):
    def construct(self):
        background, bg_text = layout()
        self.add(background)  

        # Add text as a fixed background element
        self.add(bg_text)
        self.wait()
        font_title_size= 45
        font_regular_size = 23
        
        buff=0.275   
        title = MarkupText(" መእተዊ \n",font="Nyala", font_size=font_title_size).to_edge(UP)
        self.play(Write(title), run_time=.5)
        line = Line(5*LEFT, 5*RIGHT, color=[YELLOW, BLUE]).next_to(title, DOWN,buff=buff)
        self.play(Create(line))
        ### Axiom
        axiom = MarkupText("ግሁድ \n",font="Nyala", font_size=font_regular_size).next_to(line, 2*DOWN,buff=buff)
        self.play(Write(axiom))
        self.wait()
        item1 = MarkupText("ብዘይ መረጋገጺ ከምሓቂ ዝውሰድ ሓሳብ",font="Nyala", font_size=font_title_size)
        item2 =  MarkupText("ባዕሉ ንባዕሉ ዘይጓነፅ",font="Nyala", font_size=font_title_size)
        item3 = MarkupText("ዓርሱ ዝኻኣለ",font="Nyala", font_size=font_title_size)
        item4 = MarkupText("ሙሉእነት ዘለዎ",font="Nyala", font_size=font_title_size)
    
        # Create bullet points as simple Text or Dot mobjects
        bullet1 = Text('•', font_size=font_title_size)
        bullet2 = Text('•', font_size=font_title_size)
        bullet3 = Text('•', font_size=font_title_size)
        bullet4 = Text('•', font_size=font_title_size)
        list_items = VGroup(
            VGroup(bullet1, item1).arrange(RIGHT, buff=0.2),
            VGroup(bullet2, item2).arrange(RIGHT, buff=0.2),
            VGroup(bullet3, item3).arrange(RIGHT, buff=0.2),
            VGroup(bullet4, item4).arrange(RIGHT, buff=0.2)
        ).arrange(DOWN, aligned_edge=LEFT)

        for row in list_items:
            self.play(Write(row))
            self.wait(.5)
        self.wait()
        self.play(FadeOut(axiom), FadeOut(list_items), run_time=1)
        self.wait(1)
        # Abstraction in action 
        img_1 = "assets/woman-brushing-teeth-svgrepo-com.svg" 
        img_2 = "assets/woman-doing-gymnastics-at-home-svgrepo-com.svg"
        img_3 = "assets/woman-doing-yoga-meditation-svgrepo-com.svg"
        img_4 = "assets/woman-getting-up-svgrepo-com.svg"
        img_5 = "assets/woman-shopping-svgrepo-com.svg"
        image_files = [
            img_1,
            img_2,
            img_3,
            img_4,
            img_5 ,
        ]
        # 2. Create an empty VGroup to hold the images.
        images_group = VGroup()
        group1 = VGroup()
        group2 = VGroup()
        group3 = VGroup()
        group1.add(SVGMobject(img_1))
        group1.add(SVGMobject(img_2))
        
        group2.add(SVGMobject(img_3))
        group2.add(SVGMobject(img_4))
        
        group3.add(SVGMobject(img_5))
        
        title1 = MarkupText(" ብምድሪ መጓዓዝያ",font="Nyala", font_size=font_title_size).next_to(group1, UP)
        title2 = MarkupText(" ብባሓሪ መጓዓዝያ",font="Nyala", font_size=font_title_size).next_to(group2, UP)
        title3 = MarkupText(" ብኣየር መጓዓዝያ",font="Nyala", font_size=font_title_size).next_to(group3, UP)
        transport = MarkupText("መጓዓዝያ",font="Nyala", font_size=font_title_size).move_to(ORIGIN)
        letter_x = MarkupText("ሀ",font="Nyala", font_size=font_title_size).move_to(ORIGIN)

        final_group1 = VGroup(title1, group1)
        final_group2 = VGroup(title2, group2)
        final_group3 = VGroup(title3, group3)
        
        side_length = 8
        height = side_length * np.sqrt(3) / 2
        
        # Calculate the vertex coordinates relative to the scene's center.
        # Top vertex
        top_pos = np.array([0, height / 2, 0])
        # Bottom-left vertex
        bottom_left_pos = np.array([-side_length / 2, -height / 2, 0])
        # Bottom-right vertex
        bottom_right_pos = np.array([side_length / 2, -height / 2, 0])
        
        final_group1.move_to(top_pos)
        final_group2.move_to(bottom_left_pos)
        final_group3.move_to(bottom_right_pos)
        all_groups = VGroup(final_group1, final_group2, final_group3).arrange(buff=1)
        # 3. Use a loop to create and position each ImageMobject randomly.
        for image_file in image_files:
            # Create an ImageMobject from the file.
            img = SVGMobject(image_file)

            # Get the size of the screen.
            frame_height = self.camera.frame_height # type: ignore
            frame_width = self.camera.frame_width # type: ignore

            # Generate random x and y coordinates within the screen bounds.
            # `np.random.uniform(low, high)` is perfect for this.
            # Adjust the range to prevent images from spawning partially off-screen.
            random_x = np.random.uniform(-frame_width/2 + img.width/2, frame_width/2 - img.width/2) # type: ignore
            random_y = np.random.uniform(-frame_height/2 + img.height/2, frame_height/2 - img.height/2) # type: ignore
            
            # Set the image's position to the random coordinates.
            img.move_to(random_x * RIGHT + random_y * UP)
            
            # You can also apply other random properties, like scale and rotation.
            # img.scale(np.random.uniform(0.5, 1.5))
            # img.rotate(np.random.uniform(0, 2 * PI))

            # Add the image to the group.
            images_group.add(img)
            
        self.play(FadeIn(images_group), run_time=1)
        self.wait(1)
        
        self.play(
            ReplacementTransform(images_group[0], final_group1.submobjects[1][0]),
            ReplacementTransform(images_group[1], final_group1.submobjects[1][1]),
            ReplacementTransform(images_group[2], final_group2.submobjects[1][0]),
            ReplacementTransform(images_group[3], final_group2.submobjects[1][1]),
            ReplacementTransform(images_group[4], final_group3.submobjects[1][0]),
            Write(title1),
            Write(title2),
            Write(title3),
            
            run_time=2
        )
        # self.play(FadeOut(images_group))
        self.wait(1)
        self.play(ReplacementTransform(all_groups, transport), run_time=1.5)
        self.wait(1)
        # self.play(FadeOut(all_groups))
        self.play(ReplacementTransform(transport, letter_x), run_time=1.5)
        self.wait(1)
        # self.play(FadeOut(transport))
        self.play(FadeOut(letter_x), run_time=1)
        self.wait(1)
        
        
        ### Abstraction
        abstraction = MarkupText("ኣርቅቆ \n",font="Nyala", font_size=font_regular_size).next_to(line, 2*DOWN,buff=buff)
        self.play(Write(abstraction))
        self.wait()
        item1 = MarkupText("መለለዪ ሓባራዊ ቅዲ",font="Nyala", font_size=font_title_size)
        item2 =  MarkupText("ሓፈሻዊ ክልሰ-ሓሳብ ንምፍጣር",font="Nyala", font_size=font_title_size)
        item3 = MarkupText("ዝተሓላለኸ ሓሳብ ንምቕላል",font="Nyala", font_size=font_title_size)
        item4 = MarkupText("ሓሳባት ብምስሊ ንምውካል",font="Nyala", font_size=font_title_size)
    
        # Create bullet points as simple Text or Dot mobjects
        bullet1 = Text('•', font_size=font_title_size)
        bullet2 = Text('•', font_size=font_title_size)
        bullet3 = Text('•', font_size=font_title_size)
        bullet4 = Text('•', font_size=font_title_size)
        list_items = VGroup(
            VGroup(bullet1, item1).arrange(RIGHT, buff=0.2),
            VGroup(bullet2, item2).arrange(RIGHT, buff=0.2),
            VGroup(bullet3, item3).arrange(RIGHT, buff=0.2),
            VGroup(bullet4, item4).arrange(RIGHT, buff=0.2)
        ).arrange(DOWN, aligned_edge=LEFT)

        for row in list_items:
            self.play(Write(row))
            self.wait(.5)
        self.wait()
        self.play(FadeOut(abstraction), FadeOut(list_items), run_time=1)
        self.wait(1)
        
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

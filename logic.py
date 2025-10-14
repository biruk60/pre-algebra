
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
        
from manim import *

class HistoryTimeline(Scene):
    def construct(self):
        # Timeline horizontal line
        timeline = Line(LEFT*6, RIGHT*6, stroke_width=4)

        # Milestone data: (x, year, color, icon, title, desc, position)
        milestones = [
            (-5, "2017", BLUE, "✈️", "Title Here", "Description text commonly used as placeholder", DOWN),
            (-2, "2019", YELLOW, "🚀", "Title Here", "Description text commonly used as placeholder", UP),
            (0, "2021", PINK, "⏳", "Title Here", "Description text commonly used as placeholder", DOWN),
            (3, "2023", BLUE, "🎯", "Title Here", "Description text commonly used as placeholder", UP),
        ]

        self.add(timeline)
        dots = []
        for x, year, color, icon, title, desc, position in milestones:
            # Marker dot
            dot = Dot(point=[x, 0, 0], color=color, radius=0.13)
            dots.append(dot)

            # Vertical connector
            line = Line([x, 0, 0], [x, 1.8 if position==UP else -1.8, 0], stroke_width=3, color=color)
            self.add(dot, line)

            # Icon in circle
            circ = Circle(radius=0.65, color=color, stroke_width=3)
            circ.move_to([x, 1.2 if position==UP else -1.2, 0])
            icon_text = Text(icon, font_size=60)
            icon_text.move_to(circ.get_center())
            self.add(circ, icon_text)

            # Year text
            year_text = Text(year, font_size=54, color=GREY_A, weight=BOLD)
            year_text.next_to(circ, UP if position==UP else DOWN)
            self.add(year_text)

            # Title
            title_text = Text(title, font_size=32, color=WHITE, weight=BOLD)
            title_text.next_to(year_text, DOWN)
            self.add(title_text)

            # Sub-description text
            desc_text = Text(desc, font_size=18, color=GREY_C, line_spacing=0.7)
            desc_text.next_to(title_text, DOWN)
            desc_text.align_to(title_text, LEFT)
            self.add(desc_text)

        # Optionally animate the scene constructively
        self.wait(2) 

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
        axiom = MarkupText("ግሁድ \n",font="Nyala", font_size=40).next_to(line, 2*DOWN,buff=buff)
        self.play(Write(axiom))
        self.wait()
        item1 = MarkupText("ብዘይ መረጋገጺ ከምሓቂ ዝውሰድ ሓሳብ",font="Nyala", font_size=font_regular_size)
        item2 =  MarkupText("ባዕሉ ንባዕሉ ዘይጓነፅ",font="Nyala", font_size=font_regular_size)
        item3 = MarkupText("ዓርሱ ዝኻኣለ",font="Nyala", font_size=font_regular_size)
        item4 = MarkupText("ሙሉእነት ዘለዎ",font="Nyala", font_size=font_regular_size)
    
        # Create bullet points as simple Text or Dot mobjects
        bullet1 = Text('•', font_size=font_regular_size)
        bullet2 = Text('•', font_size=font_regular_size)
        bullet3 = Text('•', font_size=font_regular_size)
        bullet4 = Text('•', font_size=font_regular_size)
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
        
        scale = .40
        # Abstraction in action 
        img_1 = SVGMobject("assets/svgs/airplane.svg").scale(scale) 
        img_2 = SVGMobject("assets/svgs/bike.svg").scale(scale)
        img_3 = SVGMobject("assets/svgs/boat.svg").scale(scale)
        img_4 = SVGMobject("assets/svgs/bus.svg").scale(scale)
        img_5 = SVGMobject("assets/svgs/car.svg").scale(scale)
        img_6 = SVGMobject("assets/svgs/drone.svg").scale(scale)


        img_7 = SVGMobject("assets/svgs/express.svg").scale(scale)
        img_8 = SVGMobject("assets/svgs/freighter.svg").scale(scale)
        img_9 = SVGMobject("assets/svgs/helicopter.svg").scale(scale)
        img_10 = SVGMobject("assets/svgs/hot-air-balloon.svg").scale(scale)
        img_11 = SVGMobject("assets/svgs/jet.svg").scale(scale)
        img_12 = SVGMobject("assets/svgs/minibus.svg").scale(scale)

        img_13 = SVGMobject("assets/svgs/motorbike.svg").scale(scale) 
        img_14 = SVGMobject("assets/svgs/rail.svg").scale(scale)
        img_15 = SVGMobject("assets/svgs/rocket.svg").scale(scale)
        img_16 = SVGMobject("assets/svgs/sailboat.svg").scale(scale)
        img_17 = SVGMobject("assets/svgs/scooter.svg").scale(scale)
        img_18 = SVGMobject("assets/svgs/ship-cruise.svg").scale(scale)

        img_19 = SVGMobject("assets/svgs/ship.svg").scale(scale) 
        img_20 = SVGMobject("assets/svgs/submarine.svg").scale(scale)
        img_21 = SVGMobject("assets/svgs/subway.svg").scale(scale)
        img_22 = SVGMobject("assets/svgs/train.svg").scale(scale)
        img_23 = SVGMobject("assets/svgs/tricycle.svg").scale(scale)
        img_24 = SVGMobject("assets/svgs/truck.svg").scale(scale)

        img_0 = SVGMobject("assets/svgs/place-holder.svg").scale(scale).set_opacity(0)
        img_01 = SVGMobject("assets/svgs/place-holder.svg").scale(scale).set_opacity(0)
        img_02 = SVGMobject("assets/svgs/place-holder.svg").scale(scale).set_opacity(0)
        img_03 = SVGMobject("assets/svgs/place-holder.svg").scale(scale).set_opacity(0)
        img_04 = SVGMobject("assets/svgs/place-holder.svg").scale(scale).set_opacity(0)
        img_05 = SVGMobject("assets/svgs/place-holder.svg").scale(scale).set_opacity(0)
        img_06 = SVGMobject("assets/svgs/place-holder.svg").scale(scale).set_opacity(0)
        img_07 = SVGMobject("assets/svgs/place-holder.svg").scale(scale).set_opacity(0)
        img_08 = SVGMobject("assets/svgs/place-holder.svg").scale(scale).set_opacity(0)
        
       
        
        svgs = [img_1, img_2, img_3, img_4, img_5, img_6,
            img_7, img_8, img_9, img_10, img_11, img_12,
            img_13, img_14, img_15, img_16, img_17, img_18,
            img_19, img_20, img_21, img_22, img_23, img_24]  # image1.svg to image24.svg
        # svgs = [SVGMobject(file).scale(scale) for file in image_files]
        
        # Group the SVG objects; VGroup is used for vector graphics compatibility
        images_group = VGroup(*svgs)
        
        # Arrange in a grid: 4 rows, 6 columns
        images_group.arrange_in_grid(rows=4, cols=6, buff=0.3).next_to(line, 2*DOWN,buff=buff)  # adjust buff for spacing       
        self.play(FadeIn(images_group), run_time=1)
        self.wait(1)
       
        
        # 2. Create an empty VGroup to hold the images.
        
        cycle = VGroup()
        car = VGroup()
        train = VGroup()
        civil_plane = VGroup()
        military_plane =VGroup()
        passanger_ship = VGroup()
        cargo_ship = VGroup()
        military_ship = VGroup()
        

        cycle.add(img_2)
        cycle.add(img_13)
        cycle.add(img_17)  
        cycle.add(img_23)        
        cycle.arrange(DOWN, buff=.5)
        cycle_title = MarkupText(" ሳይክል",font="Nyala", font_size=16).next_to(cycle, UP)
        cycle_group = VGroup(cycle_title, cycle)

        car.add(img_4)
        car.add(img_5)
        car.add(img_12)
        car.add(img_24)
        car.arrange(DOWN, buff=.5)
        car_title = MarkupText(" መኪና",font="Nyala", font_size=16).next_to(car, UP)
        car_group = VGroup(car_title, car)

        train.add(img_7)
        train.add(img_14)
        train.add(img_21)
        train.add(img_22)
        train.arrange(DOWN, buff=.5)
        train_title = MarkupText(" ባቡር",font="Nyala", font_size=16).next_to(train, UP)
        train_group = VGroup(train_title, train)

        civil_plane.add(img_1)
        civil_plane.add(img_10)
        civil_plane.add(img_15)
        civil_plane.add(img_0)
        civil_plane.arrange(DOWN, buff=.5)
        civil_plane_title = MarkupText(" ናይ ገያሻይ ነፈርቲ",font="Nyala", font_size=16).next_to(civil_plane, UP)
        civil_plane_group = VGroup(civil_plane_title, civil_plane)

        military_plane.add(img_6)
        military_plane.add(img_9)
        military_plane.add(img_11)
        military_plane.add(img_01)
        military_plane.arrange(DOWN, buff=.5)
        military_plane_title = MarkupText(" ወታህደራዊ ነፈርቲ",font="Nyala", font_size=16).next_to(military_plane, UP)
        military_plane_group = VGroup(military_plane_title, military_plane)
        
        passanger_ship.add(img_3)
        passanger_ship.add(img_18)
        passanger_ship.add(img_19)
        passanger_ship.add(img_02)
        passanger_ship.arrange(DOWN, buff=.5)
        passanger_ship_title = MarkupText(" ናይ ገያሻይ መርከብ",font="Nyala", font_size=16).next_to(passanger_ship, UP)
        passanger_ship_group = VGroup(passanger_ship_title, passanger_ship)

        cargo_ship.add(img_8)
        cargo_ship.add(img_03)
        cargo_ship.add(img_04)
        cargo_ship.add(img_05)
        cargo_ship.arrange(DOWN, buff=.5)
        cargo_ship_title = MarkupText(" ናይ ፅዕነት መርከብ",font="Nyala", font_size=16).next_to(cargo_ship, UP)
        cargo_ship_group = VGroup(cargo_ship_title, cargo_ship)

        military_ship.add(img_20)
        military_ship.add(img_06)
        military_ship.add(img_07)
        military_ship.add(img_08)
        military_ship.arrange(DOWN, buff=.5)
        military_ship_title = MarkupText(" ወታህደራዊ መርከብ",font="Nyala", font_size=16).next_to(military_ship, UP)
        military_ship_group = VGroup(military_ship_title, military_ship)

        cycle_img =SVGMobject("assets/svgs/cycle-group.svg").scale(scale)
        cycle_img_group_title = MarkupText(" ሳይክል",font="Nyala", font_size=20).next_to(cycle_img, UP)
        cycle_img_group =VGroup(cycle_img_group_title,cycle_img)
        
        car_img= SVGMobject("assets/svgs/car-group.svg").scale(scale)
        car_img_group_title = MarkupText(" መኪና",font="Nyala", font_size=20).next_to(car_img, UP)
        car_img_group= VGroup(car_img_group_title, car_img)

        train_img= SVGMobject("assets/svgs/train-group.svg").scale(scale)
        train_img_group_title = MarkupText(" ባቡር",font="Nyala", font_size=20).next_to(train_img, UP)
        train_img_group= VGroup(train_img_group_title, train_img )

        plane_img=SVGMobject("assets/svgs/civil-plane-group.svg").scale(scale)
        plane_img_group_title = MarkupText("ነፋሪት",font="Nyala", font_size=20).next_to(plane_img, UP) 
        plane_img_group=VGroup(plane_img_group_title,plane_img ) 

        ship_img = SVGMobject("assets/svgs/ship-group.svg").scale(scale)
        ship_img_group_title = MarkupText("መርከብ",font="Nyala", font_size=20).next_to(ship_img, UP)
        ship_img_group = VGroup(ship_img_group_title, ship_img)

        ground_img= SVGMobject("assets/svgs/road.svg").scale(scale)
        ground_transport_title = MarkupText(" ብምድሪ መጓዓዝያ",font="Nyala", font_size=23).next_to(ground_img, UP)
        ground_transport = VGroup(ground_transport_title, ground_img)        
        
        air_img= SVGMobject("assets/svgs/cloud.svg").scale(scale)
        air_transport_title = MarkupText(" ብኣየር መጓዓዝያ",font="Nyala", font_size=23).next_to(air_img, UP)
        air_transport = VGroup(air_transport_title, air_img)

        water_img= SVGMobject("assets/svgs/water.svg").scale(scale) 
        water_transport_title = MarkupText(" ብባሓሪ መጓዓዝያ",font="Nyala", font_size=23).next_to(water_img, UP)         
        water_transport = VGroup(water_transport_title, water_img )


        all_groups = VGroup(cycle_group,
                            car_group,
                            train_group,
                            civil_plane_group,
                            military_plane_group,
                            passanger_ship_group,
                            cargo_ship_group,
                            military_ship_group,
                            ).arrange_in_grid(rows=4, cols=8, buff=0.3).next_to(line, 2*DOWN,buff=buff)
       
        self.play(
            
            ReplacementTransform(images_group[1], cycle_group.submobjects[1][0]),
            ReplacementTransform(images_group[12], cycle_group.submobjects[1][1]),
            ReplacementTransform(images_group[16], cycle_group.submobjects[1][2]),
            ReplacementTransform(images_group[22], cycle_group.submobjects[1][3]),
            ReplacementTransform(images_group[3], car_group.submobjects[1][0]),
            ReplacementTransform(images_group[4], car_group.submobjects[1][1]),
            ReplacementTransform(images_group[11], car_group.submobjects[1][2]),
            ReplacementTransform(images_group[23], car_group.submobjects[1][3]),
            ReplacementTransform(images_group[6], train_group.submobjects[1][0]),
            ReplacementTransform(images_group[13], train_group.submobjects[1][1]),
            ReplacementTransform(images_group[20], train_group.submobjects[1][2]),
            ReplacementTransform(images_group[21], train_group.submobjects[1][3]),

            ReplacementTransform(images_group[0], civil_plane_group.submobjects[1][0]),
            ReplacementTransform(images_group[9], civil_plane_group.submobjects[1][1]),
            ReplacementTransform(images_group[15], civil_plane_group.submobjects[1][2]),

            ReplacementTransform(images_group[5], military_plane_group.submobjects[1][0]),
            ReplacementTransform(images_group[8], military_plane_group.submobjects[1][1]),
            ReplacementTransform(images_group[10], military_plane_group.submobjects[1][2]),

            ReplacementTransform(images_group[2], passanger_ship_group.submobjects[1][0]),
            ReplacementTransform(images_group[17], passanger_ship_group.submobjects[1][1]),
            ReplacementTransform(images_group[18], passanger_ship_group.submobjects[1][2]),
            ReplacementTransform(images_group[7], cargo_ship_group.submobjects[1][0]),
            ReplacementTransform(images_group[19], military_ship_group.submobjects[1][0]),
           
            Write(cycle_title),
            Write(car_title),
            Write(train_title),    
            Write(civil_plane_title), 
            Write(military_plane_title),
            Write(passanger_ship_title),    
            Write(cargo_ship_title), 
            Write(military_ship_title), 
                    
            run_time=1
        )
        
        self.wait(1)
               
        all_generic_groups = VGroup(cycle_img_group,
                                    car_img_group,
                                    train_img_group,
                                    ship_img_group,
                                    plane_img_group,
                                    ).arrange_in_grid(rows=1, cols=5, buff=0.3)
        self.play(
            ReplacementTransform(all_groups, all_generic_groups),  
            FadeOut(cycle_title),
            FadeOut(car_title),
            FadeOut(train_title),    
            FadeOut(civil_plane_title), 
            FadeOut(military_plane_title),
            FadeOut(passanger_ship_title),    
            FadeOut(cargo_ship_title), 
            FadeOut(military_ship_title),             
            Write(cycle_img_group_title),
            Write(car_img_group_title),
            Write(train_img_group_title),    
            Write(plane_img_group_title), 
            Write(ship_img_group_title),          
            run_time=1
        )       
        
        self.wait(1)
        all_transportation_groups = VGroup(ground_transport,
                                           air_transport,
                                           water_transport,
                                           ).arrange_in_grid(rows=1, cols=3, buff=0.5)
        
        self.play(           
            ReplacementTransform(all_generic_groups, all_transportation_groups),  
            FadeOut(cycle_img_group_title),
            FadeOut(car_img_group_title),
            FadeOut(train_img_group_title),    
            FadeOut(plane_img_group_title), 
            FadeOut(ship_img_group_title),  

            Write(ground_transport_title),            
            Write(air_transport_title),   
            Write(water_transport_title),  
            
            run_time=1
        )
        self.wait(1)
        
        transport_title = MarkupText("መጓዓዝያ",font="Nyala", font_size=40)
        letter_a_title = MarkupText(" ሀ ",font="Nyala", font_size=40)
        # transport = VGroup(transport_title).move_to(ORIGIN)
        self.play(ShrinkToCenter(all_transportation_groups), run_time=1)
        self.wait()

        self.play(Write(transport_title), run_time=1)
        self.wait()
        self.play(Unwrite(transport_title), run_time=1)
        # self.play(Unwrite(transport_title), FadeOut(transport), run_time=1)
        
        self.wait()
        self.play( Write(letter_a_title), run_time=.5)
        
                        
        self.play(FadeOut(letter_a_title), run_time=1)
        
        self.wait()
        
        
        ### Abstraction
        abstraction = MarkupText("ኣርቅቆ \n",font="Nyala", font_size=font_title_size).next_to(line, 2*DOWN,buff=buff)
        self.play(Write(abstraction))
        self.wait()
        item1 = MarkupText("መለለዪ ሓባራዊ ቅዲ",font="Nyala", font_size=font_regular_size)
        item2 =  MarkupText("ሓፈሻዊ ክልሰ-ሓሳብ ንምፍጣር",font="Nyala", font_size=font_regular_size)
        item3 = MarkupText("ዝተሓላለኸ ሓሳብ ንምቕላል",font="Nyala", font_size=font_regular_size)
        item4 = MarkupText("ሓሳባት ብምስሊ ንምውካል",font="Nyala", font_size=font_regular_size)
    
        # Create bullet points as simple Text or Dot mobjects
        bullet1 = Text('•', font_size=font_regular_size)
        bullet2 = Text('•', font_size=font_regular_size)
        bullet3 = Text('•', font_size=font_regular_size)
        bullet4 = Text('•', font_size=font_regular_size)
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
        
        
 # manim -ql -p --disable_caching  -o table_of_content.mp4 logic.py TableOfContents
 # manim -ql -p --disable_caching  -o introduction.mp4 logic.py Introduction

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

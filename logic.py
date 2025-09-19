
from manim import * 
import manimpango

class TOCAnimation(Scene):
    def construct(self):
        # Sections for the table of contents
        sections = [
            "Introduction",
            "Background",
            "Methods",
            "Results",
            "Discussion",
            "Conclusion"
        ]
        
        # Create Text mobjects for each section
        section_texts = [Text(s, font_size=36) for s in sections]
        
        # Arrange vertically with some spacing
        toc = VGroup(*section_texts).arrange(DOWN, aligned_edge=LEFT, buff=0.7)
        
        # Create a background rectangle for each text for highlighting
        highlights = VGroup(*[
            Rectangle(width=text.width+0.5, height=text.height+0.2, fill_opacity=0, fill_color=YELLOW, stroke_width=0)
            for text in section_texts
        ])
        
        # Position highlights behind texts
        for rect, text in zip(highlights, section_texts):
            rect.move_to(text.get_center())
        
        # Group highlights and texts to add to scene
        grouped = VGroup(highlights, *section_texts)
        self.add(grouped)
        
        # Animate highlighting each section one by one
        for i in range(len(sections)):
            # Highlight current section
            self.play(
                highlights[i].animate.set_fill(YELLOW, opacity=0.5),
                run_time=1
            )
            
            # Wait so highlight is visible
            self.wait(1)
            
            # Remove highlight before moving to next, except last
            if i < len(sections) - 1:
                self.play(
                    highlights[i].animate.set_fill(YELLOW, opacity=0),
                    run_time=0.5
                )
        
        # Keep final highlight visible for a moment
        self.wait(2)


        
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

from manim import *
import numpy as np

class Skibidi2(Scene):
    def construct(self):

        self.add(Text(f"Period of a Pendulum", font_size=60).to_edge(UP).set_color(WHITE))

        # Clock Body
        everything = VGroup()
        body = Rectangle(height=4, width=2, color=WHITE).shift(DOWN * 1)

        # Clock Head
        head = Square(side_length=1.5, color=WHITE).next_to(body, UP, buff=0)

        # Clock Face
        clock_face = Circle(radius=0.6, color=WHITE).move_to(head.get_center())

        # Clock Ticks (12-hour markers)
        tick_marks = VGroup()
        for i in range(12):
            angle = i * (360 / 12) * DEGREES
            start = clock_face.get_center()
            end = clock_face.point_at_angle(angle)
            new_start = interpolate(start, end, 0.7)
            new_end = interpolate(start, end, 0.9)
            tick = Line(new_start, new_end, color=WHITE)
            tick_marks.add(tick)
        start = clock_face.get_center()
        end = clock_face.point_at_angle(PI/2)
        new_start = interpolate(start, end, 0)
        new_end = interpolate(start, end, 0.9)
        tick = Line(new_start, new_end, color=WHITE)
        tick_marks.add(tick)
        start = clock_face.get_center()
        end = clock_face.point_at_angle(PI/1.4)
        new_start = interpolate(start, end, 0)
        new_end = interpolate(start, end, 0.6)
        tick = Line(new_start, new_end, color=WHITE)
        tick_marks.add(tick)

        self.add(body, head, clock_face, tick_marks)

        # Pendulum
        # Pendulum pivot
        pivot = body.get_top() + DOWN * 0.5  

        # Angle Tracker for dynamic movement
        angle_tracker = ValueTracker(0)

        # Pendulum rod
        def get_rod():
            angle = angle_tracker.get_value()
            return Line(pivot, pivot + 2.5 * np.array([np.sin(angle), -np.cos(angle), 0]), color=WHITE)

        rod = always_redraw(get_rod)

        # Pendulum bob
        def get_bob():
            angle = angle_tracker.get_value()
            bob_position = pivot + 2.5 * np.array([np.sin(angle), -np.cos(angle), 0])
            return Circle(radius=0.2, color=WHITE).move_to(bob_position)

        bob = always_redraw(get_bob)

        # Add to scene
        self.add(rod, bob)

        self.wait(1)

        # Pendulum Animation (Oscillates smoothly)
        self.play(angle_tracker.animate.set_value(15 * DEGREES), run_time=0.01, rate_func=smooth)
        self.play(angle_tracker.animate.set_value(-15 * DEGREES), run_time=1, rate_func=rate_functions.smooth)
        self.play(angle_tracker.animate.set_value(15 * DEGREES), run_time=1, rate_func=rate_functions.smooth)
        self.play(angle_tracker.animate.set_value(-15 * DEGREES), run_time=1, rate_func=rate_functions.smooth)
        self.play(angle_tracker.animate.set_value(0), run_time=1, rate_func=rate_functions.smooth)

        everything.add(body, head, clock_face, tick_marks, rod, bob)

        everything.generate_target()
        everything.target.shift(5*LEFT)

        pivot += 5*LEFT
        
        self.add(everything)
        self.play(MoveToTarget(everything))
        
        rod2 = Line(pivot, [pivot[0], pivot[1] - 2.5, pivot[2]])
        self.add(rod2)
        
        self.play(rod2.animate.set_color(RED), run_time=1)


        text_L = MathTex(r"L").set_color(RED)
        text_L.font_size = 72

        # Transform the rod into the text "L" at its new position
        self.play(TransformMatchingShapes(rod2, text_L), run_time=1)
        self.wait(0.5)

        

        text_eq = MathTex(r"T = 2\pi\sqrt{\frac{L}{g}}").set_color(RED).shift(RIGHT*2)
        text_eq.font_size = 72
        # self.add(text_eq.to_edge(RIGHT))

        self.play(TransformMatchingShapes(text_L, text_eq), run_time=1)
        self.wait(0.5)
        # self.add(Text(f"a.get_start() = amogus", font_size=24).to_edge(UR).set_color(YELLOW))
        self.wait(5)


# class SwingingPendulum(Scene):
#     def construct(self):
#         # Create clock body
#         swing_body = Circle(radius=1, color=WHITE)
#         swing_head = Dot(swing_body.get_top(), color=WHITE)

#         # Clock face details
#         clock_face = VGroup(swing_body, swing_head)
#         tick_marks = VGroup(*[Line(ORIGIN, UP * 0.1).move_to(swing_body.point_at_angle(a)) for a in np.linspace(0, TAU, 12)])

#         # Pendulum pivot
#         pivot = swing_body.get_bottom() + UP * 4  

#         # Angle Tracker for dynamic movement
#         angle_tracker = ValueTracker(0)

#         # Pendulum rod
#         def get_rod():
#             angle = angle_tracker.get_value()
#             return Line(pivot, pivot + 2.5 * np.array([np.sin(angle), -np.cos(angle), 0]), color=WHITE)

#         rod = always_redraw(get_rod)

#         # Pendulum bob
#         def get_bob():
#             angle = angle_tracker.get_value()
#             bob_position = pivot + 2.5 * np.array([np.sin(angle), -np.cos(angle), 0])
#             return Circle(radius=0.2, color=WHITE).move_to(bob_position)

#         bob = always_redraw(get_bob)

#         # Add to scene
#         self.add(swing_body, swing_head, clock_face, tick_marks, rod, bob)

#         # Pendulum Animation (Oscillates smoothly)
#         self.play(angle_tracker.animate.set_value(20 * DEGREES), run_time=1, rate_func=smooth)
#         self.play(angle_tracker.animate.set_value(-20 * DEGREES), run_time=1, rate_func=smooth)
#         self.play(angle_tracker.animate.set_value(0), run_time=1, rate_func=smooth)

#         # Loop animation
#         self.play(
#             angle_tracker.animate.set_value(20 * DEGREES).set_rate_func(rate_functions.ease_in_out_sine),
#             angle_tracker.animate.set_value(-20 * DEGREES).set_rate_func(rate_functions.ease_in_out_sine),
#             run_time=2, rate_func=rate_functions.ease_in_sine
#         )

#         self.wait(5)

# class TransformObjectToText(Scene):
#     def construct(self):
#         # Create an initial object (e.g., a square)
#         square = Square(color=BLUE).scale(2)
        
#         # Create the text, initially transparent
#         text = Text("Hello, Manim!", font_size=48)
#         text.set_opacity(0)  # Start fully transparent
        
#         # Position text at the square's location
#         text.move_to(square.get_center())

#         # Animate the transformation
#         self.play(Transform(square, text), text.animate.set_opacity(1), run_time=2)

#         # Hold the final frame for clarity
#         self.wait(2)


# class Skibidi(Scene):
#     def construct(self):
#         circle = Circle()
#         square = Square()
#         triangle = Triangle()

#         circle.shift(LEFT)
#         square.shift(UP)
#         triangle.shift(RIGHT)
#         # constants.

#         # place the circle two units left from the origin
#         circle.move_to(LEFT * 2)
#         # place the square to the left of the circle
#         square.next_to(circle, LEFT)
#         # align the left border of the triangle to the left border of the circle
#         triangle.align_to(circle, LEFT)

#         circle.set_stroke(color=GREEN, width=20)
#         square.set_fill(YELLOW, opacity=1.0)
#         triangle.set_fill(PINK, opacity=0.5)
#         # only VMobject can set_fill, Mobject can only do set_color

#         self.add(triangle, square, circle)
#         # order matters, triangle is in the back
#         self.wait(1)

# class SquareToCircle(Scene):
#     def construct(self):
#         circle = Circle()  # create a circle
#         circle.set_fill(PINK, opacity=0.5)  # set color and transparency

#         square = Square()  # create a square
#         square.rotate(PI / 4)  # rotate a certain amount

#         self.play(Create(square))  # animate the creation of the square
#         self.play(Transform(square, circle))  # interpolate the square into the circle
#         self.play(FadeOut(square))  # fade out animation

# class SquareAndCircle(Scene):
#     def construct(self):
#         circle = Circle()  # create a circle
#         circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

#         square = Square()  # create a square
#         square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

#         square.next_to(circle, RIGHT, buff=0.5)  # set the position
#         self.play(Create(circle), Create(square))  # show the shapes on screen

# class AnimatedSquareToCircle(Scene):
#     def construct(self):
#         circle = Circle()  # create a circle
#         square = Square()  # create a square

#         self.play(Create(square))  # show the square on screen
#         self.play(square.animate.rotate(PI / 4))  # rotate the square
#         self.play(Transform(square, circle))  # transform the square into a circle
#         self.play(
#             square.animate.set_fill(PINK, opacity=0.5)
#         )  # color the circle on screen

# class DifferentRotations(Scene):
#     def construct(self):
#         left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
#         right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
#         self.play(
#             left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
#         )
#         self.wait()

# class TwoTransforms(Scene):
#     def transform(self):
#         a = Circle()
#         b = Square()
#         c = Triangle()
#         # transform makes the points of a mapped to b
#         self.play(Transform(a, b))
#         self.play(Transform(a, c))
#         self.play(FadeOut(a))

#     def replacement_transform(self):
#         a = Circle()
#         b = Square()
#         c = Triangle()
#         # replace transform literally replaces a with b instead
#         self.play(ReplacementTransform(a, b))
#         self.play(ReplacementTransform(b, c))
#         self.play(FadeOut(c))

#     def construct(self):
#         self.transform()
#         self.wait(0.5)  # wait for 0.5 seconds
#         self.replacement_transform()

# class Sections(Scene):
#     def construct(self):
#         self.next_section()
#         self.add(Circle())
#         # now we wait 1sec and have an animation to satisfy the section
#         self.wait()
#         self.next_section("this is an optional name that doesn't have to be unique")
#         self.add(Square())
#         self.wait()
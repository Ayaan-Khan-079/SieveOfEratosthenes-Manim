%%manim -qm SieveOfEratosthenes

from manim import *

class SieveOfEratosthenes(Scene):
    def construct(self):
        N = 50  # Maximum number
        grid_size = 10  # Grid width

        # Create number grid
        numbers = VGroup()
        number_objects = []
        for i in range(2, N + 1):
            num = Integer(i).scale(0.7)
            num.move_to(((i - 2) % grid_size, -((i - 2) // grid_size), 0))
            numbers.add(num)
            number_objects.append(num)

        # Center the grid
        numbers.move_to(ORIGIN)

        # Title
        title = Tex("Sieve of Eratosthenes")
        title.move_to(UP * 3)  # Position the title above
        self.play(Write(title))
        self.wait(1)

        # Create initial fade-in effect for the grid
        self.play(FadeIn(numbers))
        self.wait(1)

        # Prime colors for marking multiples
        prime_colors = {
            2: RED,
            3: GREEN,
            5: BLUE,
            7: YELLOW
        }

        # Sieve algorithm: Start with 2 and mark non-primes
        for prime in prime_colors:
            self.play(number_objects[prime-2].animate.set_color(prime_colors[prime]))
            self.wait(0.5)

            for i in range(prime * 2, N + 1, prime):
                num_to_mark = number_objects[i-2]
                if num_to_mark.get_color() != prime_colors[prime]:  # If the number is not already marked
                    self.play(num_to_mark.animate.set_color(prime_colors[prime]), run_time=0.3)
                    self.wait(0.1)

        # After marking, change the prime numbers to a distinct color (WHITE) and bold them
        for prime in prime_colors:
            self.play(number_objects[prime-2].animate.set_color(WHITE).scale(1.2))
            self.wait(0.3)

        # Final pause before the video ends
        self.wait(3)

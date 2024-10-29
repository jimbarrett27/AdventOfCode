from util.input import get_input
from dataclasses import dataclass

@dataclass
class Reindeer:

    name: str
    speed: int
    endurance: int
    recovery_period: int

    position: int = 0
    time_in_phase: int = 0
    current_phase: str = 'running'

test_input = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
"""

def part_1():
    
    puzzle_input = get_input(2015, 14)

    reindeers = []
    for line in puzzle_input.splitlines():
        words = line.split()
        reindeers.append(Reindeer(
            name=words[0],
            speed=int(words[3]),
            endurance=int(words[6]),
            recovery_period=int(words[-2])
        ))

    for time in range(2503):
        for reindeer in reindeers:
            if reindeer.current_phase == 'running':
                if reindeer.time_in_phase == reindeer.endurance:
                    reindeer.current_phase = 'resting'
                    reindeer.time_in_phase = 0
                    continue
                reindeer.position += reindeer.speed

            elif reindeer.current_phase == 'resting':
                if reindeer.time_in_phase == reindeer.recovery_period:
                    reindeer.current_phase = 'running'
                    reindeer.time_in_phase = 0
                    continue

            reindeer.time_in_phase += 1
        
    print('\n'.join(map(str,reindeers)))

    winning_reindeer = max(reindeers, key=lambda x: x.position)

    return winning_reindeer.position

def part_2():
    pass
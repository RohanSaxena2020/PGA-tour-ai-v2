# PGA-tour-statistics-v2: A linear regresson ML model trained on 2024 PGA tour data

This model is designed to predict a golfer's scoring average based on four inputs.

## Background Part 1

The PGA Tour, which is the highest level of professional golf similar to the NFL or MLB, has an 8-month season. Throughout the season, players work to accumulate FedEx Cup points by winning or finishing well at different tournaments. The season ends with a final tournament called the Tour Championship.

The Tour Championship works differently than most golf tournaments. In most tournaments, all players start at the same score (Even Par or E). However, the Tour Championship features a strokes-based system that was started in 2019. Under this system, the player with the most FedEx Cup points prior to the Tour Championship starts at -10 (Ten Under Par), while second place starts at -8, third place starts at -7, all the way down to players 26-30 starting at E. 

This means that if you have more FedEx Cup points prior to starting the tournament, you have a big advantage over the rest of the field. Winning the Tour Championship also comes with a hefty prize ($25 million as of 2024). Therefore, it's not just important to win on the PGA Tour, but also to perform well throughout the season to accumulate a lot of FedEx Cup points and give yourself the best chance of winning.

One of the best measures of how consistently well a player is performing is their Scoring Average (i.e., the average score they shoot).

## Background Part 2

The PGA Tour does a great job keeping detailed statistics. One of the measures they use is called "Strokes Gained," which breaks down into multiple categories:

- **Strokes Gained Off the Tee**: The first shot you hit.
- **Strokes Gained Approach**: After you hit your first shot, the shot(s) you hit onto the green.
- **Strokes Gained Around the Green**: When you miss the green, how well you perform.
- **Strokes Gained Putting**: How well you putt.
- **Strokes Gained Tee to Green**: A holistic measure of how good you aree ball striking (from the tee, approach the green, around the green).
- **Birdie Average**: How many birdies you make per round. A birdie is when you go 1 less than par on a hole (2 on a Par 3, 3 on a Par 4, 4 on a Par 5). 
- **Driving Distance**: How far you hit the ball on your first shot (on average).
- **GIR (Green In Regulation Percentage)**: Green in regulation is did you hit the green in Par-2 strokes. (1 stroke on a Par 3, 2 strokes on a Par 4, 3 strokes on a Par 5)

How Strokes Gained works is that for each shot a player hits, they will compare that shot to the average PGA Tour player's performance. If the player did better than the PGA Tour average, they will "gain strokes." If they did worse than the PGA Tour average, they will "lose strokes."

The easiest example to explain this is a simple 3-foot putt. On average, PGA Tour players make 96% of 3-foot putts (according to research by Columbia University professor Mark Broadie). If a player makes a 3-foot putt, they gain 0.04 strokes on the field. If they miss a 3-foot putt, they lose 0.96 strokes.

### Hope that makes sense!!

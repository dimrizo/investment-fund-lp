# investment-fund-lp
# A simple investments allocation problem solved with a Linear Programming (LP) model and Google OR-tools, including a sensitivity analysis.

----
The R&C Fund has just obtained 142600€ and is looking for investment opportunities. All new investments will either be made in oil, steel, or Greek government bonds. The corresponding expected rate of return for each investment type is given as:\
\
Investment 	Project Rate of Return (%)\
Atlantic Oil: 2.5\
Pacific Oil: 6.5\
Midwest Steel: 7.2\
Huber Steel: 7.4\
Greek Government Bonds: 3.7\
\
Furthermore, the R&C Fund management imposes the following investment requirements:

1 - The overall investment amount in the oil industry should not be more than 60300€.

2 - The overall investment amount in the steel industry should not be more than 82300€.

3 - The overall investment amount in Greek Government bonds should be at least 25% of the overall available funds that will be invested in the steel industry.

4 - The investment in Pacific Oil, the high-return but high-risk investment, cannot be more than 60% of the total oil investment.

----
**Questions:**\
A) Formulate a linear program (clearly define your decision variables) to maximize the projected returns for this investment problem.\
B) Calculate the optimal solution by using a LP problem solver.\
C) Sensitivity analysis: Calculate the shadow price for each constraint and the reduced cost for each variable.

** Math model included in lp_math_model.md. Answers to B & C are given when python script is run! **

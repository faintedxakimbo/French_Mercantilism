# Load necessary libraries
library(ggplot2)

# Demand curve parameters
a1 <- 112
b1 <- 21.54
a2 <- 276
b2 <- 100.57
MC <- 0

# Create a sequence of Q
Q <- seq(0, 120, length.out = 200)

# Inverse demand functions
P1 <- (a1 - Q) / b1
P2 <- (a2 - Q) / b2

# Maximum prices
p_max_oligop <- a1 / b1
p_max_compet <- a2 / b2

# Surplus calculations
Producer_surplus_oligopoly <- 56 * 2.6
Consumer_suplus_oligopoly <- 0.5 * ((p_max_oligop - 2.6) * 56)
Producer_surplus_compet <- 100 * 1.75
Consumer_surplus_compet <- 0.5 * ((p_max_compet - 1.75) * 100)

# Create a data frame for ggplot
df <- data.frame(Q = Q, P1 = P1, P2 = P2)

# Surplus & DWL areas
Q1 <- 56
Q2 <- 100
P1_val <- 2.6
P2_val <- 1.75
dwl_triangle <- 0.5 * (P1_val - P2_val) * (Q2 - Q1)
dwl_rectangle <- (Q2 - Q1) * P2_val
total_dwl <- dwl_triangle + dwl_rectangle

# Data frames for filled areas
df_fill1 <- data.frame(Q = seq(0, Q1, length.out = 200))
df_fill1$P1 <- (a1 - df_fill1$Q) / b1

df_fill2 <- data.frame(Q = seq(0, Q2, length.out = 200))
df_fill2$P2 <- (a2 - df_fill2$Q) / b2

df_gap <- data.frame(Q = seq(Q1, Q2, length.out = 200))
df_gap$P1_gap <- (a1 - df_gap$Q) / b1
df_gap$P2_gap <- (a2 - df_gap$Q) / b2

# Plotting with ggplot2
ggplot() +
  geom_line(data = df, aes(x = Q, y = P1), color = "blue", size = 1, linetype = "solid") +
  geom_line(data = df, aes(x = Q, y = P2), color = "green", size = 1, linetype = "solid") +
  geom_point(aes(x = 56, y = 2.6), color = "red", size = 3) +
  geom_point(aes(x = 100, y = 1.75), color = "purple", size = 3) +

  # Consumer surplus under oligopoly
  geom_ribbon(data = df_fill1, aes(x = Q, ymin = 2.6, ymax = P1), fill = "#66c2a5", alpha = 0.6) +
  # Producer surplus under oligopoly
  geom_ribbon(data = df_fill1, aes(x = Q, ymin = 0, ymax = 2.6), fill = "#fc8d62", alpha = 0.6) +
  # Producer surplus under smuggler
  geom_ribbon(data = df_fill2, aes(x = Q, ymin = 0, ymax = 1.75), fill = "#ffd92f", alpha = 0.6) +
  # DWL triangle
  geom_ribbon(data = df_gap, aes(x = Q, ymin = P2_gap, ymax = P1_gap), fill = "#e78ac3", alpha = 0.7) +
  # DWL rectangle
  geom_ribbon(data = df_gap, aes(x = Q, ymin = 0, ymax = P2_gap), fill = "#a6d854", alpha = 0.5) +

  labs(title = "Inverse Demand Curves (Guild vs Smuggler)",
       x = "Quantity (Q)", y = "Price (Livre Tournois)") +
  theme_minimal() +
  coord_cartesian(xlim = c(0, 120), ylim = c(0, 5)) +
  theme(legend.position = "none") # Can customize legend if needed

# Print surplus and DWL
cat("Oligopoly Demand Curve: Q = 112 - 21.54P\n")
cat("Smuggler Demand Curve: Q = 276 - 100.57P\n")
cat("Producer Surplus under Oligopoly: ", Producer_surplus_oligopoly, "\n")
cat("Consumer Surplus under Oligopoly: ", Consumer_suplus_oligopoly, "\n")
cat("Producer Surplus under Smuggler: ", Producer_surplus_compet, "\n")
cat(sprintf("DWL Triangle: %.2f\n", dwl_triangle))
cat(sprintf("DWL Rectangle: %.2f\n", dwl_rectangle))
cat(sprintf("Total DWL: %.2f\n", total_dwl))

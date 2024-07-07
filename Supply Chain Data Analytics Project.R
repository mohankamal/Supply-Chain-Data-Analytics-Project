# Load necessary libraries
library(readxl)

# Load the Excel dataset
df <- read_excel("C:\\Users\\mohan\\Downloads\\Supply Chain Project\\SupplyChainDataAnalyticsProject.xlsx")
df
# View the structure of the dataset
str(df)

# Check dimensions (rows and columns)
cat("Number of rows:", nrow(df), "\n")
cat("Number of columns:", ncol(df), "\n")

# Summary statistics
summary(df)

# Check for missing values
cat("Missing values:\n")
print(colSums(is.na(df)))

# Optionally, clean data (e.g., remove rows with missing values)
# Example: Remove rows with any NA values
clean_df <- na.omit(df)
clean_df

# Convert date column if necessary (assuming 'date_column' is your date column)
df$`Order Date` <- as.Date(df$`Order Date`, format = "%m/%d/%Y")

#1. Linear Regression
#Linear regression models the relationship between the dependent variable
#(sales) and one or more independent variables (such as discount and profit).

# Fit linear regression model
lm_model <- lm(Sales ~ Discount + Profit, data = df)

# Predict sales for the next 2 years (adjust 'newdata' accordingly)
newdata <- data.frame(Discount = 0.1, Profit = 500)  # Example new data
predicted_sales <- predict(lm_model, newdata = newdata, interval = "predict", n.ahead = 2 * 365)


#Decision trees can capture nonlinear relationships and interactions between variables.



# Load necessary libraries
library(rpart)

# Fit decision tree model
tree_model <- rpart(Sales ~ Discount + Profit, data = df)

# Predict sales for the next 2 years
predicted_sales <- predict(tree_model, newdata = newdata, type = "vector")


#3. Random Forest
#Random forests improve prediction accuracy by combining multiple decision trees.


#Random Forest Random forests improve prediction accuracy by combining multiple decision trees.



# Load necessary libraries (if not loaded)
library(randomForest)

# Fit random forest model
rf_model <- randomForest(Sales ~ Discount + Profit, data = df)

# Predict sales for the next 2 years
predicted_sales <- predict(rf_model, newdata = newdata)


#4. Time Series Forecasting (ARIMA)
#ARIMA models are specifically designed for time series data, capturing trends and seasonal patterns.



# Convert to time series object
ts_data <- ts(df$Sales, frequency = 12)  # Assuming monthly data

#install.packages("forecast")
library(forecast)

# Fit ARIMA model
arima_model <- auto.arima(ts_data)

# Forecast sales for the next 24 months (2 years)
forecast_values <- forecast(arima_model, h = 24)

# Extract predicted sales
predicted_sales <- forecast_values$mean

#  ------------------------------------------------------------



# Load necessary libraries
library(dplyr)
library(ggplot2)

city_sales <- df %>%
  group_by(City, `Ship Mode`) %>%
  summarise(Total_Sales = sum(Sales)) %>%
  ungroup()

# Find the city with the highest sales
top_city <- city_sales %>%
  group_by(City) %>%
  summarise(Total_Sales = sum(Total_Sales)) %>%
  arrange(desc(Total_Sales)) %>%
  slice(1) %>%
  pull(City)

# Filter the data for the top city
top_city_data <- df %>% filter(City == top_city)

# Print the top city
print(top_city)

# Assuming you have already executed the code to find `top_city` and `top_city_data`

# Calculate total sales by ship mode in the top city
shipmode_sales <- top_city_data %>%
  group_by(`Ship Mode`) %>%
  summarise(Total_Sales = sum(Sales)) %>%
  arrange(desc(Total_Sales))


# Assuming ship modes are: "airway", "roadways", "seaways", "railways"

# Convert Total_Sales to numeric format if necessary (to avoid scientific notation)
shipmode_sales$Total_Sales <- as.numeric(shipmode_sales$Total_Sales)



#----------------------------------------------
# Prompting and Interactively user to enter a state name to display the Slea data in Shipping Mode

selected_state <- "Florida"
selected_state

# Filter data for the selected state
state_data <- df %>%
  filter(State == selected_state)

# Calculate total sales by ship mode in the selected state
shipmode_sales <- state_data %>%
  group_by(`Ship Mode`) %>%
  summarise(Total_Sales = sum(Sales)) %>%
  arrange(desc(Total_Sales))

# Plotting the bar chart
ggplot(shipmode_sales, aes(x = `Ship Mode`, y = Total_Sales, fill = `Ship Mode`)) +
  geom_bar(stat = "identity") +
  scale_fill_manual(values = c("#9933FF", "#33FFFF", "red", "darkblue"), name = "Ship Mode") +  # Assign colors defined above and add legend name
  geom_text(aes(label = scales::comma(Total_Sales), y = Total_Sales), vjust = -0.5, size = 3, color = "black") +  # Add sales labels on top of bars
  labs(title = paste("Total Sales by Ship Mode in", selected_state),
       x = "Ship Mode", y = "Total Sales") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +  # Rotate x-axis labels
  scale_y_continuous(labels = scales::comma)  # Format y-axis labels with commas





selected_state <- "New York"
selected_state

# Filter data for the selected state
state_data <- df %>%
  filter(State == selected_state)

# Calculate total sales by ship mode in the selected state
shipmode_sales <- state_data %>%
  group_by(`Ship Mode`) %>%
  summarise(Total_Sales = sum(Sales)) %>%
  arrange(desc(Total_Sales))

# Plotting the bar chart
ggplot(shipmode_sales, aes(x = `Ship Mode`, y = Total_Sales, fill = `Ship Mode`)) +
  geom_bar(stat = "identity") +
  scale_fill_manual(values = c("#9933FF", "#33FFFF", "red", "darkblue"), name = "Ship Mode") +  # Assign colors defined above and add legend name
  geom_text(aes(label = scales::comma(Total_Sales), y = Total_Sales), vjust = -0.5, size = 3, color = "black") +  # Add sales labels on top of bars
  labs(title = paste("Total Sales by Ship Mode in", selected_state),
       x = "Ship Mode", y = "Total Sales") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +  # Rotate x-axis labels
  scale_y_continuous(labels = scales::comma)  # Format y-axis labels with commas



#--------------------------------

# Calculate total sales by ship mode across all states
shipmode_sales_all <- df %>%
  group_by(State, `Ship Mode`) %>%
  summarise(Total_Sales = sum(Sales)) %>%
  ungroup() %>%
  group_by(`Ship Mode`) %>%
  summarise(Total_Sales = sum(Total_Sales)) %>%
  arrange(desc(Total_Sales))

# Plotting the bar chart
ggplot(shipmode_sales_all, aes(x = `Ship Mode`, y = Total_Sales, fill = `Ship Mode`)) +
  geom_bar(stat = "identity") +
  scale_fill_manual(values = c("#9933FF", "#33FFFF", "red", "darkblue"), name = "Ship Mode") +  # Assign colors defined above and add legend name
  geom_text(aes(label = scales::comma(Total_Sales), y = Total_Sales), vjust = -0.5, size = 3, color = "black") +  # Add sales labels on top of bars
  labs(title = "Total Sales by Ship Mode Across All States",
       x = "Ship Mode", y = "Total Sales") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +  # Rotate x-axis labels
  scale_y_continuous(labels = scales::comma)  # Format y-axis labels with commas








































################## Rough Practce R COde ##############################################

# Plotting the bar chart with represeting the sales for each Ship Mode.

ggplot(shipmode_sales, aes(x = `Ship Mode`, y = Total_Sales, fill = `Ship Mode`)) +
  geom_bar(stat = "identity") +
  scale_fill_manual(values = c("#9933FF", "#33FFFF", "red", "darkblue"), name = "Ship Mode") +  # Assign colors defined above and add legend name
  geom_text(aes(label = scales::comma(Total_Sales), y = Total_Sales), vjust = -0.5, size = 3, color = "black") +  # Add sales labels on top of bars
  labs(title = paste("Total Sales by Ship Mode in", top_city),
       x = "Ship Mode", y = "Total Sales") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +  # Rotate x-axis labels
  scale_y_continuous(labels = scales::comma)  # Format y-axis labels with commas



ggplot(shipmode_sales, aes(x = `Ship Mode`, y = Total_Sales, fill = `Ship Mode`)) +
  geom_bar(stat = "identity") +
  scale_fill_manual(values = c("#9933FF", "#33FFFF", "red", "darkblue"), name = "Ship Mode") +  # Assign colors defined above and add legend name
  geom_text(aes(label = scales::comma(Total_Sales), y = Total_Sales), vjust = -0.5, size = 3, color = "black") +  # Add sales labels on top of bars
  labs(title = "Total Sales by Ship Mode",
       x = "Ship Mode", y = "Total Sales") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +  # Rotate x-axis labels
  scale_y_continuous(labels = scales::comma)  # Format y-axis labels with commas


# Plotting the bar chart
#ggplot(shipmode_sales, aes(x = `Ship Mode`, y = Total_Sales)) +
# geom_bar(stat = "identity", fill = "skyblue") +
#  labs(title = paste("Total Sales by Ship Mode in", top_city),
#      x = "Ship Mode", y = "Total Sales") +
#  theme_minimal() +
#  theme(axis.text.x = element_text(angle = 45, hjust = 1))  # Rotate x-axis labels for better readability


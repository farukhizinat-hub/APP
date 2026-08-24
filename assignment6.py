# 0/1 Knapsack using Bottom-Up and Top-Down Dynamic Programming


# ---------------- BOTTOM-UP APPROACH ----------------

def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):

            # If current item can fit
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Find selected items
    selected_items = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i)
            w -= weights[i - 1]

    selected_items.reverse()

    return dp[n][capacity], selected_items


# ---------------- TOP-DOWN APPROACH ----------------

def knapsack_top_down(weights, values, capacity):
    n = len(weights)

    # Memoization table
    memo = {}

    def solve(i, remaining_capacity):

        # Base case
        if i == 0 or remaining_capacity == 0:
            return 0

        # Return stored result if already calculated
        if (i, remaining_capacity) in memo:
            return memo[(i, remaining_capacity)]

        # If current item is too heavy
        if weights[i - 1] > remaining_capacity:
            result = solve(i - 1, remaining_capacity)

        else:
            # Maximum of including or excluding the item
            include = values[i - 1] + solve(
                i - 1,
                remaining_capacity - weights[i - 1]
            )

            exclude = solve(i - 1, remaining_capacity)

            result = max(include, exclude)

        # Store result
        memo[(i, remaining_capacity)] = result

        return result

    max_value = solve(n, capacity)

    return max_value


# ---------------- MAIN PROGRAM ----------------

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

print("Weights:", weights)
print("Values:", values)
print("Capacity:", capacity)

# Bottom-Up
max_value_bottom, selected_items = knapsack_bottom_up(
    weights, values, capacity
)

print("\n--- Bottom-Up Dynamic Programming ---")
print("Maximum Value:", max_value_bottom)
print("Selected Item Numbers:", selected_items)

# Top-Down
max_value_top = knapsack_top_down(
    weights, values, capacity
)

print("\n--- Top-Down Dynamic Programming ---")
print("Maximum Value:", max_value_top)
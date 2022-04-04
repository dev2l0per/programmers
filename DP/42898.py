# #include <string>
# #include <vector>

# using namespace std;

# const int MAX = 101;

# int dp[MAX][MAX];

# int solution(int m, int n, vector<vector<int>> puddles) {
#     int answer = 0;
    
#     dp[1][1] = 1;
#     for (int i = 0; i < puddles.size(); i++)
# 		dp[puddles[i][1]][puddles[i][0]] = -1;
#     for (int i = 1; i <= n; i++)
#     {
#         for (int j = 1; j <= m; j++)
#         {
#             if (!dp[i][j])
#             {
#                 if (dp[i - 1][j] == -1)
#                 {
#                     dp[i][j] = dp[i][j - 1];
#                 }
#                 else if (dp[i][j - 1] == -1)
#                 {
#                     dp[i][j] = dp[i - 1][j];
#                 }
#                 else
#                 {
#                     dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
#                 }
#             }
#         }
#     }
    
#     answer = dp[n][m] % 1000000007;
    
#     return answer;
# }
class Solution {
public:
    int countCompleteComponents(int n, vector<vector<int>>& edges) {
        vector<vector<int>> adj(n);
        for (auto& e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        
        vector<bool> visited(n, false);
        int completeCount = 0;
        
        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                vector<int> component;
                queue<int> q;
                q.push(i);
                visited[i] = true;
                
                while (!q.empty()) {
                    int u = q.front(); q.pop();
                    component.push_back(u);
                    for (int v : adj[u]) {
                        if (!visited[v]) {
                            visited[v] = true;
                            q.push(v);
                        }
                    }
                }
                
                long long V = component.size();
                long long E = 0;
                for (int node : component) E += adj[node].size();
                
                if (E == V * (V - 1)) completeCount++;
            }
        }
        return completeCount;
    }
};
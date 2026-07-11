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
                vector<int> q = {i};
                visited[i] = true;
                int head = 0;
                while(head < q.size()){
                    int u = q[head++];
                    component.push_back(u);
                    for(int v : adj[u]){
                        if(!visited[v]){
                            visited[v] = true;
                            q.push_back(v);
                        }
                    }
                }
                long long v = component.size();
                long long e = 0;
                for(int node : component) e += adj[node].size();
                if (e / 2 == v * (v - 1) / 2) completeCount++;
            }
        }
        return completeCount;
    }
};
#include <bits/stdc++.h>
using namespace std;
int n, a[300002],r[300002],b[300002],red,blue;
 
vector<int>g[300002];
 
void dfs(int v, int p) {
    r[v] = a[v] == 1;
    b[v] = a[v] == 2;
    for(int u : g[v]) {
        if(u == p) continue;
        dfs(u, v);
        r[v] += r[u];
        b[v] += b[u];
    }
}
 
 
int main() {
	cin>>n;
	for(int i=1;i<=n;i++){
		cin>>a[i];
		red+=a[i]==1;
		blue+=a[i]==2;
	}
	for(int i=1;i<n;i++){
		int x,y;
		cin>>x>>y;
		g[x].push_back(y);
		g[y].push_back(x);
	}
	int ans=0;
	dfs(1,0);
	for(int i=2;i<=n;i++){
		if((r[i]==r[1]&&b[i]==0)||(b[i]==b[1]&&r[i]==0))
			ans++;
	}
	cout<<ans<<endl;
	return 0;
}
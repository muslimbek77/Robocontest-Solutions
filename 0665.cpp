#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct Fenwick {
    int n;
    vector<ll> f;
    Fenwick(int _n): n(_n), f(n+1,0) {}
    void upd(int i, ll v){
        for(; i<=n; i += i&-i) f[i] += v;
    }
    ll query(int i){
        ll s=0;
        for(; i>0; i -= i&-i) s += f[i];
        return s;
    }
    ll rangeQuery(int l, int r){
        if(l>r) return 0;
        return query(r) - query(l-1);
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    cin >> n >> q;
    vector<ll> a(n+1), b(n+1);
    for(int i=1;i<=n;i++) cin>>a[i];
    for(int i=1;i<=n;i++) cin>>b[i];

    // 1) prefix sums
    vector<ll> A(n+1,0), B(n+1,0), D(n+1,0);
    for(int i=1;i<=n;i++){
        A[i] = A[i-1] + a[i];
        B[i] = B[i-1] + b[i];
        D[i] = A[i] - B[i];
    }

    // 2) tayyorlaymiz (D_i, i)
    vector<pair<ll,int>> events;
    events.reserve(n);
    for(int i=1;i<=n;i++){
        events.emplace_back(D[i], i);
    }
    sort(events.begin(), events.end(),
         greater<pair<ll,int>>());

    // 3) so'rovlarni o'qib, offline ro'yxat
    struct Query { ll T; int l,r,id; };
    vector<Query> qs(q);
    for(int i=0;i<q;i++){
        int l,r;
        cin>>l>>r;
        ll T = D[l-1];
        qs[i] = {T, l, r, i};
    }
    sort(qs.begin(), qs.end(),
         [](auto &x, auto &y){ return x.T > y.T; });

    // 4) uchta Fenwick: count, sumA, sumB
    Fenwick ftCnt(n), ftA(n), ftB(n);

    vector<ll> ans(q);
    int ptr = 0;
    for(auto &Q: qs){
        // qo'sh. D_i >= Q.T bo'lganlarni BITga
        while(ptr < n && events[ptr].first >= Q.T){
            int idx = events[ptr].second;
            ftCnt.upd(idx, 1);
            ftA.upd(idx, A[idx]);
            ftB.upd(idx, B[idx]);
            ptr++;
        }
        // BITdan [l,r]
        ll c_ge = ftCnt.rangeQuery(Q.l, Q.r);
        ll SA_ge = ftA.rangeQuery(Q.l, Q.r);
        ll SB_ge = ftB.rangeQuery(Q.l, Q.r);

        ll len = Q.r - Q.l + 1;
        ll c_lt = len - c_ge;

        ll totalB = B[Q.r] - B[Q.l-1];
        ll SB_lt = totalB - SB_ge;

        ll baseA = A[Q.l-1];
        ll baseB = B[Q.l-1];

        ans[Q.id] = (SA_ge - c_ge*baseA) + (SB_lt - c_lt*baseB);
    }

    // natijalarni chiqarish
    for(int i=0;i<q;i++){
        cout << ans[i] << "\n";
    }
    return 0;
}

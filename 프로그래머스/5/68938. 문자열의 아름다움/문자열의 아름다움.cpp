#include <string>
#include <vector>

using namespace std;

struct Node {
    int alpha;
    int length;
};

Node stNode[300000];
int NodeCnt;

struct Entry
{
    int Length;
    int Count;
};

Entry stTable[26][300000];
int EntryCnt[26];

long long Calc(int s_len, int e_len)
{
    int N, K;
    if (s_len > e_len)
    {
        N = e_len;
        K = s_len;
    }
    else
    {
        N = s_len;
        K = e_len;
    }

    if (N == 1) return N * K;

    return ((N + K + 1) * (N + 1) * N / 2) - ((N + 1) * N * (2 * N + 1) / 3);
}

long long MaxBeauty(long long size)
{
    if (size == 1)
        return 0;

    return ((size * size * (size - 1)) / 2) - ((size - 1) * size * ((2 * size) - 1) / 6);
}

long long solution(string s) {
    long long answer = 0;

    answer = MaxBeauty(s.size());

    int len = 1;
    stNode[NodeCnt].alpha = s[0];

    for (int i = 1; i < s.size(); i++)
    {
        if (stNode[NodeCnt].alpha == s[i])
        {
            len++;
        }
        else
        {
            stNode[NodeCnt++].length = len;
            stNode[NodeCnt].alpha = s[i];
            len = 1;
        }
    }
    stNode[NodeCnt++].length = len;

    if (NodeCnt == 1) return 0;

    for (int i = 0; i < NodeCnt; i++)
    {
        int idx = stNode[i].alpha - 'a';

        answer -= MaxBeauty(stNode[i].length);

        for (int j = 0; j < EntryCnt[idx]; j++)
        {
            answer -= (stTable[idx][j].Count * Calc(stTable[idx][j].Length, stNode[i].length));
        }

        int cur = 0;
        while (true)
        {
            if (stTable[idx][cur].Count == 0)
            {
                stTable[idx][cur].Length = stNode[i].length;
                stTable[idx][cur].Count++;
                EntryCnt[idx]++;
                break;
            }

            if (stTable[idx][cur].Length == stNode[i].length)
            {
                stTable[idx][cur].Count++;
                break;
            }

            cur++;
        }
    }

    return answer;
}
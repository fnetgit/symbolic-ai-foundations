#include <bits/stdc++.h>

using namespace std;

map<string, vector<string>> gostadores{
    {"joao", {"jose", "ana"}},
    {"jose", {"pedro", "joao"}},
    {"ana", {"maria", "pedro", "felipe"}},
    {"maria", {"jose", "ana", "felipe"}},
    {"pedro", {"maria", "ana"}},
    {"felipe", {"pedro", "joao"}}};

bool se_gostam()
{
    string p1, p2;
    cout << "Digite a pessoa 1: ";
    cin >> p1;
    cout << "Digite a pessoa 2: ";
    cin >> p2;

    auto it = gostadores.find(p1);
    if (it != gostadores.end())
    {
        const auto &lista = it->second;
        return find(lista.begin(), lista.end(), p2) != lista.end();
    }
    return false;
}

vector<string> gosta_de_quem()
{
    string p;
    cout << "Diga uma pessoa pra saber de quem ela gosta: ";
    cin >> p;

    if (gostadores.count(p))
     {
        return gostadores[p];
    }
    return {};
}

int main()
{
    cout << se_gostam() << "\n";

    vector<string> resultado = gosta_de_quem();
    for (const string &nome : resultado)
    {
        cout << nome << " ";
    }
    cout << "\n";
}
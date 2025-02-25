import random

def simulate_match(veriler, simulations=10000000):
    results = {"Galatasaray": 0, "Fenerbahçe": 0, "Beraberlik": 0}
    
    for _ in range(simulations):
        gs = veriler["Galatasaray"]
        fb = veriler["Fenerbahçe"]
        
        gs_power = (gs["galibiyet"] * 3 + gs["beraberlik"] + gs["attığı_gol"] - gs["yedigi_gol"] + gs["hücum_gücü"] + gs["savunma_gücü"]) * gs["form"]
        fb_power = (fb["galibiyet"] * 3 + fb["beraberlik"] + fb["attığı_gol"] - fb["yedigi_gol"] + fb["hücum_gücü"] + fb["savunma_gücü"]) * fb["form"]
        
        total_power = gs_power + fb_power
        gs_prob = gs_power / total_power
        fb_prob = fb_power / total_power
        
        outcome = random.choices(["Galatasaray", "Fenerbahçe", "Beraberlik"], weights=[gs_prob, fb_prob, 0.2])[0]
        results[outcome] += 1
    
    for team in results:
        results[team] = results[team] / simulations * 100
    
    return results

takim_verileri = {
    "Galatasaray": {
        "oynanan_maç": 23,
        "galibiyet": 20,
        "beraberlik": 3,
        "mağlubiyet": 0,
        "attığı_gol": 59,
        "yedigi_gol": 23,
        "hücum_gücü": 85,
        "savunma_gücü": 80,
        "form": 1.1  # Son dönemdeki performans çarpanı
    },
    "Fenerbahçe": {
        "oynanan_maç": 23,
        "galibiyet": 18,
        "beraberlik": 3,
        "mağlubiyet": 2,
        "attığı_gol": 60,
        "yedigi_gol": 23,
        "hücum_gücü": 83,
        "savunma_gücü": 78,
        "form": 1.0  # Son dönemdeki performans çarpanı
    }
}

prediction = simulate_match(takim_verileri)
print("Tahmini Sonuçlar:")
print(f"Galatasaray kazanma olasılığı: {prediction['Galatasaray']:.2f}%")
print(f"Fenerbahçe kazanma olasılığı: {prediction['Fenerbahçe']:.2f}%")
print(f"Beraberlik olasılığı: {prediction['Beraberlik']:.2f}%")

import random

def get_ai_suggestions(user_text: str) -> list[str]:
    """
    Simulates an AI writing assistant by offering suggestions to elaborate,
    rephrase, or expand on the user's input.
    This demonstrates AI as an 'active partner' rather than a mere text generator.
    """
    suggestions = []
    text_lower = user_text.lower()

    # --- AI as an active partner: Providing elaboration/expansion --- 
    # This section simulates AI helping to develop ideas, not just generate text.
    if "yapay zeka" in text_lower or "ai" in text_lower:
        suggestions.append(
            "Yapay zeka kavramını daha detaylı açıklamak ister misiniz? "
            "Örneğin, makine öğrenimi veya derin öğrenme arasındaki farklara değinebilirsiniz."
        )
        suggestions.append(
            "AI'ın günlük hayatımızdaki veya belirli bir sektördeki uygulamalarına odaklanarak "
            "konuyu genişletebilirsiniz."
        )
    if "yazım" in text_lower or "writing" in text_lower:
        suggestions.append(
            "Yazım sürecindeki zorluklara veya yazarların karşılaştığı yaygın sorunlara "
            "değinerek konuyu zenginleştirebilirsiniz."
        )
        suggestions.append(
            "Farklı yazım türleri (akademik, yaratıcı, teknik) arasındaki ayrımları "
            "vurgulayarak metni çeşitlendirebilirsiniz."
        )
    if "gelecek" in text_lower or "future" in text_lower:
        suggestions.append(
            "Gelecekteki olası senaryoları veya tahminleri ekleyerek okuyucunun ilgisini çekebilirsiniz."
        )
        suggestions.append(
            "Teknolojinin veya toplumun geleceği üzerindeki etkilerini tartışarak "
            "daha derin bir analiz sunabilirsiniz."
        )

    # --- AI as an active partner: Offering alternative phrasing/refinement ---
    # This section simulates AI helping to improve expression and clarity.
    if "dönemi sona erdi" in text_lower or "era ended" in text_lower:
        suggestions.append(
            "Alternatif olarak: '...dönemi bir dönüşüm sürecine girdi' veya '...yeni bir evreye geçiyor' "
            "ifadelerini kullanmayı düşünebilirsiniz."
        )
    if "tartışmalara yol açtı" in text_lower or "caused debate" in text_lower:
        suggestions.append(
            "Daha güçlü bir ifade için: '...yoğun eleştirilere maruz kaldı' veya '...geniş çaplı bir tartışmayı tetikledi' "
            "şeklinde yeniden ifade edebilirsiniz."
        )

    # Generic suggestions if no specific keywords are found
    if not suggestions:
        suggestions.append(
            "Metninizi daha ikna edici hale getirmek için somut örnekler veya vaka çalışmaları eklemeyi düşünebilirsiniz."
        )
        suggestions.append(
            "Okuyucuyu düşündürecek bir soruyla veya güçlü bir sonuç cümlesiyle "
            "paragrafınızı bitirmeyi deneyin."
        )
        suggestions.append(
            "Farklı bir bakış açısı sunarak veya karşıt argümanları ele alarak "
            "metninizi daha dengeli hale getirebilirsiniz."
        )

    # Limit to a few suggestions for clarity
    random.shuffle(suggestions)
    return suggestions[:3] # Return up to 3 diverse suggestions

if __name__ == "__main__":
    print("Yapay Zeka Destekli Yazım Asistanı (AI-Powered Writing Assistant)")
    print("---------------------------------------------------------------")
    print("Bu araç, yazdığınız metinlere yönelik geliştirme ve genişletme önerileri sunar.")
    print("AI'ın pasif bir metin üreticisi olmaktan çıkıp, yaratıcılığınızı artıran bir iş ortağı rolünü simüle eder.")
    print("\nLütfen bir cümle veya kısa bir paragraf girin (çıkmak için 'q' yazın):")

    while True:
        user_input = input("\nMetniniz: ")
        if user_input.lower() == 'q':
            break

        if not user_input.strip():
            print("Lütfen geçerli bir metin girin.")
            continue

        ai_suggestions = get_ai_suggestions(user_input)

        print("\n--- AI Asistan Önerileri ---")
        if ai_suggestions:
            for i, suggestion in enumerate(ai_suggestions):
                print(f"{i+1}. {suggestion}")
        else:
            print("Bu metin için özel bir öneri bulunamadı. Genel geliştirme ipuçları düşünebilirsiniz.")
        print("----------------------------")

    print("\nAsistan kapatıldı. İyi günler!")

#!/usr/bin/env python3
"""Fix missing/English translations in all website locale JSON files."""

import json
import os

LOCALES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'locales')

# Keys that need translation in each language
# Only including keys that are currently English in non-English locales
TRANSLATIONS = {
    'de': {
        'home_pill_languages': '23 Sprachen',
        'home_platforms_title': 'Überall verfügbar',
        'home_platforms_desc': 'iPhone, iPad, Mac und Apple Watch — Ihre Finanzen synchronisieren sich nahtlos über alle Geräte.',
        'home_privacy_title': 'Datenschutz zuerst. Immer.',
        'home_privacy_card1_title': 'Verarbeitung auf dem Gerät',
        'home_privacy_card1_desc': 'Alle Daten bleiben auf Ihrem Gerät. Keine Server, kein Tracking, kein Konto erforderlich.',
        'home_privacy_card2_title': 'iCloud-Synchronisierung',
        'home_privacy_card2_desc': 'Optionale iCloud-Synchronisierung hält Ihre Daten verschlüsselt und nur für Sie zugänglich.',
        'home_privacy_card3_title': 'Offen & Transparent',
        'home_privacy_card3_desc': 'Keine versteckten Analysen. Kein Datenverkauf. Ein Tool, das Ihre Privatsphäre respektiert.',
        'home_cta_title': 'Intelligenter Ausgaben verfolgen',
        'home_cta_watch': 'Auch auf der Apple Watch verfügbar',
        'home_cta_travel_link': 'Probiere unseren Reisebudget App Clip',
    },
    'fr': {
        'home_pill_languages': '23 langues',
        'home_platforms_title': 'Disponible partout',
        'home_platforms_desc': 'iPhone, iPad, Mac et Apple Watch — vos finances se synchronisent sur tous vos appareils.',
        'home_privacy_title': 'Confidentialité d\'abord. Toujours.',
        'home_privacy_card1_title': 'Traitement sur l\'appareil',
        'home_privacy_card1_desc': 'Toutes les données restent sur votre appareil. Pas de serveurs, pas de suivi, pas de compte requis.',
        'home_privacy_card2_title': 'Synchronisation iCloud',
        'home_privacy_card2_desc': 'La synchronisation iCloud optionnelle garde vos données cryptées et accessibles uniquement par vous.',
        'home_privacy_card3_title': 'Ouvert et transparent',
        'home_privacy_card3_desc': 'Pas d\'analyses cachées. Pas de vente de données. Juste un outil qui respecte votre vie privée.',
        'home_cta_title': 'Commencez à suivre intelligemment',
        'home_cta_watch': 'Également disponible sur Apple Watch',
        'home_cta_travel_link': 'Essayez notre App Clip de budget voyage',
    },
    'nl': {
        'home_pill_languages': '23 talen',
        'home_platforms_title': 'Overal beschikbaar',
        'home_platforms_desc': 'iPhone, iPad, Mac en Apple Watch — je financiën synchroniseren naadloos op al je apparaten.',
        'home_privacy_title': 'Privacy eerst. Altijd.',
        'home_privacy_card1_title': 'Verwerking op apparaat',
        'home_privacy_card1_desc': 'Alle gegevens blijven op je apparaat. Geen servers, geen tracking, geen account nodig.',
        'home_privacy_card2_title': 'iCloud-synchronisatie',
        'home_privacy_card2_desc': 'Optionele iCloud-sync houdt je gegevens versleuteld en alleen toegankelijk voor jou.',
        'home_privacy_card3_title': 'Open & Transparant',
        'home_privacy_card3_desc': 'Geen verborgen analytics. Geen dataverkoop. Een tool die je privacy respecteert.',
        'home_cta_title': 'Begin slimmer bij te houden',
        'home_cta_watch': 'Ook beschikbaar op Apple Watch',
        'home_cta_travel_link': 'Probeer onze Reisbudget App Clip',
    },
    'es': {
        'home_pill_languages': '23 idiomas',
        'home_platforms_title': 'Disponible en todas partes',
        'home_platforms_desc': 'iPhone, iPad, Mac y Apple Watch — tus finanzas se sincronizan en todos tus dispositivos.',
        'home_privacy_title': 'Privacidad primero. Siempre.',
        'home_privacy_card1_title': 'Procesamiento en el dispositivo',
        'home_privacy_card1_desc': 'Todos los datos se quedan en tu dispositivo. Sin servidores, sin rastreo, sin cuenta requerida.',
        'home_privacy_card2_title': 'Sincronización iCloud',
        'home_privacy_card2_desc': 'La sincronización iCloud opcional mantiene tus datos cifrados y solo accesibles para ti.',
        'home_privacy_card3_title': 'Abierto y transparente',
        'home_privacy_card3_desc': 'Sin análisis ocultos. Sin venta de datos. Una herramienta que respeta tu privacidad.',
        'home_cta_title': 'Empieza a rastrear de forma inteligente',
        'home_cta_watch': 'También disponible en Apple Watch',
        'home_cta_travel_link': 'Prueba nuestro App Clip de presupuesto de viaje',
    },
    'it': {
        'home_pill_languages': '23 lingue',
        'home_platforms_title': 'Disponibile ovunque',
        'home_platforms_desc': 'iPhone, iPad, Mac e Apple Watch — le tue finanze si sincronizzano su tutti i dispositivi.',
        'home_privacy_title': 'Privacy prima di tutto. Sempre.',
        'home_privacy_card1_title': 'Elaborazione sul dispositivo',
        'home_privacy_card1_desc': 'Tutti i dati rimangono sul dispositivo. Nessun server, nessun tracciamento, nessun account richiesto.',
        'home_privacy_card2_title': 'Sincronizzazione iCloud',
        'home_privacy_card2_desc': 'La sincronizzazione iCloud opzionale mantiene i dati crittografati e accessibili solo a te.',
        'home_privacy_card3_title': 'Aperto e trasparente',
        'home_privacy_card3_desc': 'Nessuna analisi nascosta. Nessuna vendita di dati. Uno strumento che rispetta la tua privacy.',
        'home_cta_title': 'Inizia a tracciare in modo intelligente',
        'home_cta_watch': 'Disponibile anche su Apple Watch',
        'home_cta_travel_link': 'Prova il nostro App Clip per budget di viaggio',
    },
    'ja': {
        'home_pill_languages': '23言語',
        'home_platforms_title': 'どこでも利用可能',
        'home_platforms_desc': 'iPhone、iPad、Mac、Apple Watch — すべてのデバイスで家計がシームレスに同期。',
        'home_privacy_title': 'プライバシー第一。常に。',
        'home_privacy_card1_title': 'デバイス上で処理',
        'home_privacy_card1_desc': 'すべてのデータはデバイスに保存。サーバーなし、トラッキングなし、アカウント不要。',
        'home_privacy_card2_title': 'iCloud同期',
        'home_privacy_card2_desc': 'オプションのiCloud同期でデータを暗号化し、あなただけがアクセス可能。',
        'home_privacy_card3_title': 'オープン＆透明',
        'home_privacy_card3_desc': '隠れた分析なし。データ販売なし。プライバシーを尊重するツール。',
        'home_cta_title': 'よりスマートに管理を始めよう',
        'home_cta_watch': 'Apple Watchでも利用可能',
        'home_cta_travel_link': '旅行予算App Clipを試す',
    },
    'zh-Hans': {
        'home_pill_languages': '23种语言',
        'home_platforms_title': '随处可用',
        'home_platforms_desc': 'iPhone、iPad、Mac 和 Apple Watch — 您的财务在所有设备间无缝同步。',
        'home_privacy_title': '隐私优先。始终如一。',
        'home_privacy_card1_title': '设备端处理',
        'home_privacy_card1_desc': '所有数据保存在您的设备上。无服务器、无追踪、无需账户。',
        'home_privacy_card2_title': 'iCloud 同步',
        'home_privacy_card2_desc': '可选的 iCloud 同步确保数据加密，仅您可访问。',
        'home_privacy_card3_title': '开放透明',
        'home_privacy_card3_desc': '无隐藏分析。无数据出售。尊重您隐私的工具。',
        'home_cta_title': '开始智能记账',
        'home_cta_watch': '也可在 Apple Watch 上使用',
        'home_cta_travel_link': '试用旅行预算 App Clip',
    },
    'ko': {
        'home_pill_languages': '23개 언어',
        'home_platforms_title': '어디서나 사용 가능',
        'home_platforms_desc': 'iPhone, iPad, Mac, Apple Watch — 모든 기기에서 재정이 원활하게 동기화됩니다.',
        'home_privacy_title': '프라이버시 우선. 항상.',
        'home_privacy_card1_title': '기기 내 처리',
        'home_privacy_card1_desc': '모든 데이터가 기기에 저장됩니다. 서버 없음, 추적 없음, 계정 불필요.',
        'home_privacy_card2_title': 'iCloud 동기화',
        'home_privacy_card2_desc': '선택적 iCloud 동기화로 데이터를 암호화하고 본인만 접근 가능.',
        'home_privacy_card3_title': '개방적이고 투명한',
        'home_privacy_card3_desc': '숨겨진 분석 없음. 데이터 판매 없음. 프라이버시를 존중하는 도구.',
        'home_cta_title': '스마트 추적 시작',
        'home_cta_watch': 'Apple Watch에서도 사용 가능',
        'home_cta_travel_link': '여행 예산 App Clip 체험',
    },
    'ar': {
        'home_pill_languages': '23 لغة',
        'home_platforms_title': 'متوفر في كل مكان',
        'home_platforms_desc': 'iPhone وiPad وMac وApple Watch — تتم مزامنة أموالك بسلاسة عبر جميع أجهزتك.',
        'home_privacy_title': 'الخصوصية أولاً. دائماً.',
        'home_privacy_card1_title': 'معالجة على الجهاز',
        'home_privacy_card1_desc': 'جميع البيانات تبقى على جهازك. لا خوادم، لا تتبع، لا حساب مطلوب.',
        'home_privacy_card2_title': 'مزامنة iCloud',
        'home_privacy_card2_desc': 'مزامنة iCloud الاختيارية تحافظ على بياناتك مشفرة ومتاحة لك فقط.',
        'home_privacy_card3_title': 'مفتوح وشفاف',
        'home_privacy_card3_desc': 'لا تحليلات مخفية. لا بيع بيانات. أداة تحترم خصوصيتك.',
        'home_cta_title': 'ابدأ التتبع الذكي',
        'home_cta_watch': 'متوفر أيضاً على Apple Watch',
        'home_cta_travel_link': 'جرّب App Clip لميزانية السفر',
    },
    'he': {
        'home_pill_languages': '23 שפות',
        'home_platforms_title': 'זמין בכל מקום',
        'home_platforms_desc': 'iPhone, iPad, Mac ו-Apple Watch — הכספים שלך מסתנכרנים בכל המכשירים.',
        'home_privacy_title': 'פרטיות קודמת. תמיד.',
        'home_privacy_card1_title': 'עיבוד במכשיר',
        'home_privacy_card1_desc': 'כל הנתונים נשארים במכשיר. ללא שרתים, ללא מעקב, ללא חשבון.',
        'home_cta_title': 'התחל לעקוב בחכמה',
    },
    'fa': {
        'home_pill_languages': '۲۳ زبان',
        'home_platforms_title': 'همه‌جا در دسترس',
        'home_platforms_desc': 'iPhone، iPad، Mac و Apple Watch — امور مالی شما در همه دستگاه‌ها همگام‌سازی می‌شود.',
        'home_privacy_title': 'حریم خصوصی در اولویت. همیشه.',
        'home_privacy_card1_title': 'پردازش روی دستگاه',
        'home_privacy_card1_desc': 'تمام داده‌ها روی دستگاه شما باقی می‌ماند. بدون سرور، بدون ردیابی.',
        'home_cta_title': 'مدیریت هوشمند مالی را شروع کنید',
    },
    'pt-BR': {
        'home_pill_languages': '23 idiomas',
        'home_platforms_title': 'Disponível em todos os lugares',
        'home_platforms_desc': 'iPhone, iPad, Mac e Apple Watch — suas finanças sincronizam em todos os dispositivos.',
        'home_privacy_title': 'Privacidade em primeiro lugar. Sempre.',
        'home_cta_title': 'Comece a rastrear de forma inteligente',
    },
    'hi': {
        'home_pill_languages': '23 भाषाएं',
        'home_platforms_title': 'हर जगह उपलब्ध',
        'home_platforms_desc': 'iPhone, iPad, Mac और Apple Watch — आपके वित्त सभी डिवाइस पर सिंक होते हैं।',
        'home_privacy_title': 'गोपनीयता पहले। हमेशा।',
        'home_cta_title': 'स्मार्ट ट्रैकिंग शुरू करें',
    },
    'th': {
        'home_pill_languages': '23 ภาษา',
        'home_platforms_title': 'ใช้ได้ทุกที่',
        'home_platforms_desc': 'iPhone, iPad, Mac และ Apple Watch — การเงินของคุณซิงค์อัตโนมัติบนทุกอุปกรณ์',
        'home_privacy_title': 'ความเป็นส่วนตัวมาก่อน เสมอ',
        'home_cta_title': 'เริ่มติดตามอย่างชาญฉลาด',
    },
    'vi': {
        'home_pill_languages': '23 ngôn ngữ',
        'home_platforms_title': 'Có mặt mọi nơi',
        'home_platforms_desc': 'iPhone, iPad, Mac và Apple Watch — tài chính của bạn đồng bộ trên mọi thiết bị.',
        'home_privacy_title': 'Quyền riêng tư trước tiên. Luôn luôn.',
        'home_cta_title': 'Bắt đầu theo dõi thông minh',
    },
    'tr': {
        'home_pill_languages': '23 dil',
        'home_platforms_title': 'Her yerde kullanılabilir',
        'home_platforms_desc': 'iPhone, iPad, Mac ve Apple Watch — finanslarınız tüm cihazlarınızda sorunsuz senkronize olur.',
        'home_privacy_title': 'Gizlilik öncelikli. Her zaman.',
        'home_cta_title': 'Akıllı takibe başla',
    },
    'ru': {
        'home_pill_languages': '23 языка',
        'home_platforms_title': 'Доступно везде',
        'home_platforms_desc': 'iPhone, iPad, Mac и Apple Watch — финансы синхронизируются на всех устройствах.',
        'home_privacy_title': 'Конфиденциальность прежде всего. Всегда.',
        'home_cta_title': 'Начните умный учёт',
    },
    'uk': {
        'home_pill_languages': '23 мови',
        'home_platforms_title': 'Доступно скрізь',
        'home_platforms_desc': 'iPhone, iPad, Mac та Apple Watch — ваші фінанси синхронізуються на всіх пристроях.',
        'home_privacy_title': 'Конфіденційність насамперед. Завжди.',
        'home_cta_title': 'Починайте розумний облік',
    },
    'pl': {
        'home_pill_languages': '23 języki',
        'home_platforms_title': 'Dostępny wszędzie',
        'home_platforms_desc': 'iPhone, iPad, Mac i Apple Watch — Twoje finanse synchronizują się na wszystkich urządzeniach.',
        'home_privacy_title': 'Prywatność przede wszystkim. Zawsze.',
        'home_cta_title': 'Zacznij mądre śledzenie',
    },
    'ro': {
        'home_pill_languages': '23 de limbi',
        'home_platforms_title': 'Disponibil peste tot',
        'home_platforms_desc': 'iPhone, iPad, Mac și Apple Watch — finanțele tale se sincronizează pe toate dispozitivele.',
        'home_privacy_title': 'Confidențialitate mai întâi. Mereu.',
        'home_cta_title': 'Începe urmărirea inteligentă',
    },
    'cs': {
        'home_pill_languages': '23 jazyků',
        'home_platforms_title': 'Dostupné všude',
        'home_platforms_desc': 'iPhone, iPad, Mac a Apple Watch — vaše finance se synchronizují na všech zařízeních.',
        'home_privacy_title': 'Soukromí na prvním místě. Vždy.',
        'home_cta_title': 'Začněte chytře sledovat',
    },
    'hu': {
        'home_pill_languages': '23 nyelv',
        'home_platforms_title': 'Mindenhol elérhető',
        'home_platforms_desc': 'iPhone, iPad, Mac és Apple Watch — pénzügyeid zökkenőmentesen szinkronizálódnak.',
        'home_privacy_title': 'Adatvédelem először. Mindig.',
        'home_cta_title': 'Kezdj el okosan nyomon követni',
    },
}


def main():
    updated = 0
    for lang, translations in TRANSLATIONS.items():
        path = os.path.join(LOCALES_DIR, f'{lang}.json')
        if not os.path.exists(path):
            print(f'  SKIP {lang} (file not found)')
            continue

        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        changes = 0
        for key, value in translations.items():
            if key not in data or data[key] == key or data.get(key, '').startswith('23 Language') or data.get(key, '') == TRANSLATIONS.get('en', {}).get(key, ''):
                old = data.get(key, '(missing)')
                data[key] = value
                changes += 1

        if changes > 0:
            # Sort keys for consistent output
            sorted_data = dict(sorted(data.items()))
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(sorted_data, f, ensure_ascii=False, indent=2)
                f.write('\n')
            print(f'  OK   {lang} ({changes} keys updated)')
            updated += 1
        else:
            print(f'  OK   {lang} (no changes needed)')

    print(f'\nDone — {updated} locale files updated.')


if __name__ == '__main__':
    main()

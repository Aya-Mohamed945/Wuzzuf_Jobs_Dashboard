import pandas as pd
import re

# Comprehensive Arabic to English city mapping
CITY_TRANSLATION = {
    # Major Egyptian Cities
    'القاهرة': 'Cairo',
    'الجيزة': 'Giza',
    'الإسكندرية': 'Alexandria',
    'الشرقية': 'Sharqia',
    'السويس': 'Suez',
    'المنوفية': 'Monufya',
    'الدقهلية': 'Dakahlia',
    'القليوبية': 'Qalubia',
    'البحيرة': 'Beheira',
    'مطروح': 'Matruh',
    'البحر الأحمر': 'Red Sea',
    'دمياط': 'Damietta',
    'الغربية': 'Gharbia',
    'بورسعيد': 'Bor Saaed',
    'بني سويف': 'Beni Suef',
    'المنيا': 'Minya',
    'أسوان': 'Aswan',
    'الأقصر': 'Luxor',
    'قنا': 'Qena',
    'سوهاج': 'Sohag',
    'أسيوط': 'Assiut',
    'الفيوم': 'Fayoum',
    'كفر الشيخ': 'Kafr El Sheikh',
    'الإسماعيلية': 'Ismailia',
    
    # International Cities (Arabic spellings)
    'دبي': 'Dubai',
    'أبو ظبي': 'Abu Dhabi',
    'الشارقة': 'Sharjah',
    'الدوحة': 'Doha',
    'الرياض': 'Riyadh',
    'جدة': 'Jeddah',
    'الكويت': 'Kuwait City',
    'مسقط': 'Muscat',
    'المنامة': 'Manama',
    'لندن': 'London',
    'نيويورك': 'New York City',
    'واشنطن': 'Washington',
    'لوس أنجلوس': 'Los Angeles',
    'سان فرانسيسكو': 'San Francisco',
    'شيكاغو': 'Chicago',
    'بوسطن': 'Boston',
    'طرابلس': 'Tripoli',
    'بنغازي': 'Benghazi',
    'تونس': 'Tunis',
    'الجزائر': 'Algiers',
    'الرباط': 'Rabat',
    'الدار البيضاء': 'Casablanca',
    'عمان': 'Amman',
    'بيروت': 'Beirut',
    'دمشق': 'Damascus',
    'بغداد': 'Baghdad',
    'اسطنبول': 'Istanbul',
    'أنقرة': 'Ankara',
    'برلين': 'Berlin',
    'باريس': 'Paris',
    'روما': 'Rome',
    'مدريد': 'Madrid',
    'أمستردام': 'Amsterdam',
    'بروكسل': 'Brussels',
    'جنيف': 'Geneva',
    'زيورخ': 'Zurich',
    'فيينا': 'Vienna',
    'ستوكهولم': 'Stockholm',
    'كوبنهاغن': 'Copenhagen',
    'أوسلو': 'Oslo',
    'هلسنكي': 'Helsinki',
    'موسكو': 'Moscow',
    'بكين': 'Beijing',
    'شنغهاي': 'Shanghai',
    'طوكيو': 'Tokyo',
    'سيول': 'Seoul',
    'سنغافورة': 'Singapore',
    'كوالالمبور': 'Kuala Lumpur',
    'بومباي': 'Mumbai',
    'دلهي': 'Delhi',
    'سيدني': 'Sydney',
    'ملبورن': 'Melbourne',
    'تورونتو': 'Toronto',
    'فانكوفر': 'Vancouver',
    'مونتريال': 'Montreal',
    'ساو باولو': 'Sao Paulo',
    'ريو دي جانيرو': 'Rio de Janeiro',
    'بوينس آيرس': 'Buenos Aires',
    'مكسيكو سيتي': 'Mexico City',
    'جوهانسبرغ': 'Johannesburg',
    'كيب تاون': 'Cape Town',
    'نيروبي': 'Nairobi',
    'لاغوس': 'Lagos',
    'القاهرة': 'Cairo',  # Duplicate for international context
}

# Comprehensive Arabic to English country mapping
COUNTRY_TRANSLATION = {
    'مصر': 'Egypt',
    'السعودية': 'Saudi Arabia',
    'الإمارات': 'UAE',
    'الكويت': 'Kuwait',
    'قطر': 'Qatar',
    'البحرين': 'Bahrain',
    'عمان': 'Oman',
    'العراق': 'Iraq',
    'الأردن': 'Jordan',
    'لبنان': 'Lebanon',
    'سوريا': 'Syria',
    'فلسطين': 'Palestine',
    'اليمن': 'Yemen',
    'ليبيا': 'Libya',
    'تونس': 'Tunisia',
    'الجزائر': 'Algeria',
    'المغرب': 'Morocco',
    'موريتانيا': 'Mauritania',
    'السودان': 'Sudan',
    'الصومال': 'Somalia',
    'جيبوتي': 'Djibouti',
    'جزر القمر': 'Comoros',
    'الولايات المتحدة': 'United States',
    'أمريكا': 'United States',
    'كندا': 'Canada',
    'المملكة المتحدة': 'United Kingdom',
    'بريطانيا': 'United Kingdom',
    'ألمانيا': 'Germany',
    'فرنسا': 'France',
    'إيطاليا': 'Italy',
    'إسبانيا': 'Spain',
    'البرتغال': 'Portugal',
    'هولندا': 'Netherlands',
    'بلجيكا': 'Belgium',
    'سويسرا': 'Switzerland',
    'النمسا': 'Austria',
    'السويد': 'Sweden',
    'النرويج': 'Norway',
    'الدنمارك': 'Denmark',
    'فنلندا': 'Finland',
    'أيرلندا': 'Ireland',
    'اليونان': 'Greece',
    'تركيا': 'Turkey',
    'روسيا': 'Russia',
    'أوكرانيا': 'Ukraine',
    'الصين': 'China',
    'اليابان': 'Japan',
    'كوريا الجنوبية': 'South Korea',
    'الهند': 'India',
    'باكستان': 'Pakistan',
    'إندونيسيا': 'Indonesia',
    'ماليزيا': 'Malaysia',
    'سنغافورة': 'Singapore',
    'تايلاند': 'Thailand',
    'فيتنام': 'Vietnam',
    'الفلبين': 'Philippines',
    'أستراليا': 'Australia',
    'نيوزيلندا': 'New Zealand',
    'البرازيل': 'Brazil',
    'الأرجنتين': 'Argentina',
    'تشيلي': 'Chile',
    'كولومبيا': 'Colombia',
    'المكسيك': 'Mexico',
    'جنوب أفريقيا': 'South Africa',
    'نيجيريا': 'Nigeria',
    'كينيا': 'Kenya',
    'إثيوبيا': 'Ethiopia',
}

def translate_city(city_name):
    """Translate Arabic city names to English"""
    if pd.isna(city_name) or city_name is None:
        return city_name
    
    city_str = str(city_name).strip()
    
    # Check if it's in our translation dictionary
    for ar, en in CITY_TRANSLATION.items():
        if ar in city_str:
            return en
    
    # If no translation found, return original
    return city_str

def translate_country(country_name):
    """Translate Arabic country names to English"""
    if pd.isna(country_name) or country_name is None:
        return country_name
    
    country_str = str(country_name).strip()
    
    # Check if it's in our translation dictionary
    for ar, en in COUNTRY_TRANSLATION.items():
        if ar in country_str:
            return en
    
    # If no translation found, return original
    return country_str

def clean_data(df):
    """Main cleaning function"""
    
    # Clean company names
    df['companies'] = df['companies'].str.replace('-', '').str.strip()
    
    # Clean job titles
    job_title_mappings = {
        'Data Analyst|Data Analysis|Data Analytics': 'Data Analyst',
        'Data Entry': 'Data Entry',
        'Data Engineer': 'Data Engineer',
        'Data Security': 'Data Security',
        'Software Engineer': 'Software Engineer',
        'Cloud Developer': 'Cloud Developer',
        'Data Scientist': 'Data Scientist',
        'Accounting Manager': 'Accounting Manager',
        'Accountant|Accounting': 'Accountant',
    }
    
    for pattern, replacement in job_title_mappings.items():
        df.loc[df['job_title'].str.contains(pattern, case=False, na=False), 'job_title'] = replacement
    
    # Clean work modes
    work_mode_mappings = {
        'عمل من مقر الشركة': 'On-site',
        'عمل عن بُعد': 'Remote',
        'عمل هجين': 'Hybrid',
    }
    
    for pattern, replacement in work_mode_mappings.items():
        df.loc[df['work_modes'].str.contains(pattern, case=False, na=False), 'work_modes'] = replacement
    
    # Handle None values
    df.loc[df['work_modes'].str.contains('None', case=False, na=False), 'work_modes'] = None
    
    # Clean employment types
    employment_mappings = {
        'دوام كامل': 'Full Time',
        'تدريب عملي': 'Internship',
    }
    
    for pattern, replacement in employment_mappings.items():
        df.loc[df['employment_types'].str.contains(pattern, case=False, na=False), 'employment_types'] = replacement
    
    # Extract city and country from locations
    df['locations_'] = df['locations'].str.split(",")
    df['city'] = df['locations_'].str[-2].str.strip() if len(df['locations_'].iloc[0]) > 1 else None
    df['country'] = df['locations_'].str[-1].str.strip()
    
    # Translate city names
    df['city'] = df['city'].apply(translate_city)
    
    # Translate country names
    df['country'] = df['country'].apply(translate_country)
    
    # Drop temporary column
    df = df.drop('locations_', axis=1)
    
    return df

def validate_uploaded_data(df):
    """Validate that uploaded CSV has required columns"""
    required_columns = ['job_title', 'companies', 'locations', 'employment_types', 'work_modes', 'skills']
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        return False, f"Missing required columns: {', '.join(missing_columns)}"
    
    return True, "Data validation passed!"
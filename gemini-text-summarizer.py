import os
import google.generativeai as genai

# Access your API key as an environment variable.
genai.configure(api_key=os.environ['GEMINI_API_KEY'])
# Choose a model that's appropriate for your use case.
model = genai.GenerativeModel('gemini-1.5-flash')

summarize_text = "في الاجتماع النهاردة، اتكلمنا عن تطوير نظام المكافآت في الشركة. قررنا نزيد من المكافآت الشهرية للموظفين المجتهدين. كمان، هنقدم جوائز سنوية للموظفين المتميزين في الأداء. هنحتاج نعمل نظام تقييم جديد عشان نقدر نقيس الأداء بشكل دقيق وعادل."

def summarize_text(text):
    sys_prompt = f"""
    :لخص الكلام الاتي بطريقة احترافية بحيث تشمل جميع النقاط الاساسية في قائمة نقطية
    
    {text}
    """
    responce = model.generate_content(sys_prompt)
    return responce.text

if __name__ == "__main__":
    print(summarize_text(summarize_text))

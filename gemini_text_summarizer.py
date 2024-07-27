import os
import google.generativeai as genai

# Access your API key as an environment variable.
genai.configure(api_key=os.environ['GEMINI_API_KEY'])
# Choose a model that's appropriate for your use case.
model = genai.GenerativeModel('gemini-1.5-flash')

text_to_summarize = "في الاجتماع النهاردة، اتكلمنا عن تطوير نظام المكافآت في الشركة. قررنا نزيد من المكافآت الشهرية للموظفين المجتهدين. كمان، هنقدم جوائز سنوية للموظفين المتميزين في الأداء. هنحتاج نعمل نظام تقييم جديد عشان نقدر نقيس الأداء بشكل دقيق وعادل."

def summarize_text(transcription):
    sys_prompt = f"""
    :لخص الكلام الاتي بطريقة احترافية بحيث تشمل جميع النقاط الاساسية في قائمة نقطية
    
    {transcription}
    """
    responce = model.generate_content(sys_prompt)
    return responce._result.candidates[0].content.parts[0].text

if __name__ == "__main__":
    print(summarize_text(text_to_summarize))

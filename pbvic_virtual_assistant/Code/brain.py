from openai import OpenAI

client = OpenAI(
  api_key="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"
)

you = input("Hãy đặt câu hỏi.\n ")

try:
	completion = client.chat.completions.create(
	  model="gpt-4.1-nano",
	  #store=True,
	  messages=[
	    #{"role": "user", "content": "write a haiku about ai"}    
	    {"role": "system", "content": "Bạn là một giáo viên cấp 2, vì thế bạn nên trả lời ngắn gọn và xúc tích"},
	    {"role": "user", "content": you}
	  ],
	  temperature = 0.7,
	  max_tokens = 100
	)
	

	#print(completion.choices[0].message);
	#print(completion.choices[0].message.content);
	robot_brain = completion.choices[0].message.content
except:
	robot_brain = "Tôi đang bận, vui lòng để lại lời nhắn."
print(robot_brain)

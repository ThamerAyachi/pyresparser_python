import random

paragraph_one = "[Job Title] with a drive for excellence and adaptability, I bring a passionate and collaborative spirit to every task. With a diverse skill set and a keen eye for detail, I thrive in dynamic environments. Eager to contribute my strengths to any team, I am poised to make a meaningful impact in various professional settings."

paragraph_two = "With a dedication to excellence and a proactive mindset, I approach every task with enthusiasm and determination. Thriving in diverse environments, I leverage my adaptable nature and strong work ethic to achieve optimal results. Ready to contribute positively to [Job Title] initiatives, I am prepared to make significant contributions across various professional domains."

paragraph_three = "Fueled by a commitment to continuous growth and success, I bring a results-oriented approach to every endeavor. Thriving in collaborative environments, I leverage my strong communication skills and adaptability to drive meaningful outcomes. Excited to apply my expertise across different [Job Title] roles, I am prepared to make valuable contributions in various professional settings."

paragraph_four = "Committed to delivering high-quality work with precision and efficiency, I bring a proactive approach to every challenge. With a focus on problem-solving and a collaborative mindset, I thrive in fast-paced environments where I can utilize my versatile skill set. Eager to apply my experiences to new [Job Title] challenges, I am prepared to make valuable contributions in various professional capacities."

paragraph_five = "Passionate about making a difference, I approach every task with enthusiasm and dedication. With a track record of success and a commitment to continuous growth, I bring a results-driven approach to every endeavor. Thriving in dynamic settings, I leverage my diverse skill set and keen attention to detail to achieve optimal results. Ready to contribute positively to [Job Title] teams, I am prepared to make significant contributions across various professional domains."

paragraph_six = "Driven and adaptable, I bring a passion for excellence and a collaborative spirit to every task. With a diverse skill set and a keen eye for detail, I thrive in dynamic environments. Eager to contribute my strengths to [Job Title] teams, I am poised to make a meaningful impact in various professional settings."

paragraphs = [
    paragraph_one,
    paragraph_two,
    paragraph_three,
    paragraph_four,
    paragraph_five,
    paragraph_six
]


def reform(job_title: str) -> str:
    paragraph = random.choice(paragraphs)
    return paragraph.replace("[Job Title]", job_title)


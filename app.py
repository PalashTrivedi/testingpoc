import gradio as gr
import random
import time


def respond(message, chat_history):
    # bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
    bot_message = random.choice(['''The best way to learn a musical instrument depends on your personal learning style, goals, and the type of instrument you want to play.Here are some general tips that can help you learn an instrument effectively:
    Set clear goals: Define what you want to achieve with your music lessons. Do you want to learn to play in a band, or simply enjoy playing for personal fulfillment? Setting specific goals will help you stay motivated and focused during the learning process.
    Find a good teacher: A qualified teacher can provide personalized instruction, correct bad habits, and help you progress faster. Look for a teacher who specializes in the type of music you're interested in and has experience teaching beginners.
    Practice regularly: Regular practice is essential to improve your skills on any instrument. Aim to practice at least 20-30 minutes per day, ideally in a quiet room with minimal distractions.
    Start with the basics: Begin by learning the fundamental techniques and concepts of the instrument, such as proper hand positioning, finger placement, and basic chords or scales.
    Break it down into smaller steps: Learning an instrument involves developing muscle memory and coordination between your hands and eyes. Breaking down complex tasks into smaller steps can help you build these skills gradually and avoid feeling overwhelmed.
    Listen actively: Listening to recordings of professional musicians can help you develop your ear training skills and get a sense of the overall sound and style of different instruments. Pay attention to things like tone quality, phrasing, and dynamics.
    Experiment and explore: Don't be afraid to try new things and experiment with different techniques. Playing an instrument is all about creativity and self-expression, so don't be afraid to take risks and find your own unique voice.
    Learn music theory: Understanding music theory can help you improvise, compose, and interpret music more effectively. Study topics like chord progressions, melody construction, and rhythm analysis to enhance your understanding of music.
    Stay motivated: Learning an instrument takes time and effort, so it's important to stay motivated throughout the process. Celebrate small victories along the way, set achievable milestones, and remind yourself why you started playing in the first place.Remember, everyone learns differently, so it's important to tailor your approach to your individual needs and preferences. With consistent practice, patience, and dedication, you can become proficient in any musical instrument.''',
     '''Yes, there are several great budgeting apps available that can help you manage your finances and stick to your budget. Here are some popular options:
     Mint: Mint is one of the most popular budgeting apps out there, and for good reason. It's free, easy to use, and offers a wide range of features, including bill tracking, investment monitoring, and budgeting alerts. You can connect all of your financial accounts to Mint, and it will automatically track your spending and create a budget based on your income and expenses.
     Personal Capital: Personal Capital is another highly-rated budgeting app that allows you to track your income and expenses, create a budget, and set financial goals. It also offers investment tracking and planning tools, making it a great option for those looking to optimize their investments.
     YNAB (You Need a Budget): YNAB is a budgeting app that helps you track your income and expenses and creates a budget based on your priorities. It's known for its simple, user-friendly interface and powerful features, such as automated savings rules and investment tracking.
     Pocketbook: Pocketbook is a UK-based budgeting app that allows you to track your income and expenses, create a budget, and set financial goals. It also offers investment tracking and planning tools, as well as a debt tracker to help you pay off loans and credit card balances.
     Spendee: Spendee is a budgeting app that tracks your expenses and categorizes them for easy viewing. It also offers automatic transactions import, receipt scanning, and customizable budgets.
     Wally: Wally is a budgeting app that allows you to track your income and expenses, create a budget, and set financial goals. It also offers a feature called "Wally Coach" which provides personalized advice and guidance on how to reach your financial goals.
     Toshl Finance: Toshl Finance is a comprehensive budgeting app that allows you to track your income and expenses, create a budget, and set financial goals. It also offers investment tracking and planning tools, as well as a variety of other features such as bill tracking and alerts.
     Splitwise: Splitwise is a budgeting app that makes it easy to split bills and track expenses with friends and family. It also offers a feature called "Splitting Made Easy" which allows you to easily divide costs without having to manually enter each transaction.
     These are just a few examples of the many budgeting apps available. It's a good idea to try out a few different options to see which one works best for you and your financial situation.''',
     '''Sure! There are so many amazing places to visit around the world, depending on your interests and preferences. Here are a few suggestions:
     Bali, Indonesia - Known for its beautiful beaches, temples, and vibrant culture, Bali is a popular destination for travelers. The island offers a mix of relaxation and adventure, with activities like surfing, hiking, and exploring ancient ruins.
     New Zealand - With its stunning landscapes, diverse wildlife, and friendly locals, New Zealand is a dream destination for many travelers. From the rugged mountains to the scenic coastlines, there's something for every kind of traveler in this country.
     Costa Rica - If you're looking for a nature-filled vacation, Costa Rica is the perfect choice. With its lush rainforests, exotic animals, and beautiful beaches, this Central American country offers endless opportunities for outdoor adventures.
     Japan - For a unique cultural experience, Japan is hard to beat. From the bustling streets of Tokyo to the peaceful temples of Kyoto, this country offers a glimpse into a fascinating history and culture. And with delicious food, cutting-edge technology, and welcoming people, Japan is a must-visit destination.
     Italy - Who wouldn't want to spend their vacation in Italy? With its rich history, artistic treasures, and delicious cuisine, this country has something for everyone. From Rome's Colosseum to Florence's Uffizi Gallery, Italy is a feast for the senses.
     Thailand - For a taste of Southeast Asia, Thailand is a wonderful choice. With its warm climate, beautiful beaches, and mouthwatering street food, this country offers a relaxing and exciting vacation. Plus, the friendly locals and affordable prices make it easy to fall in love with Thailand.
     Australia - From the sun-kissed beaches to the vibrant cities, Australia is a fantastic destination for travelers. With its laid-back culture, beautiful landscapes, and unique wildlife, this country offers a one-of-a-kind experience. And with a range of outdoor activities, from snorkeling to surfing, there's something for every kind of traveler.
     Of course, there are countless other destinations worth considering, but these ten should give you a good starting point for your travel plans.'''])

    chat_history.append((message, bot_message))
    time.sleep(2)
    return "", chat_history


callback = gr.CSVLogger()

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()

    # chatbot = gr.Chatbot(value=[], elem_id="chatbot")
    with gr.Row():
        msg = gr.Textbox(placeholder="👉 Enter your prompt and press ENTER", )
        clear = gr.ClearButton([msg, chatbot])
        regenerate = gr.Button(value="🔄 Regenerate")
        # txt = gr.Textbox(
        #           show_label=False,
        #           placeholder="Enter text and press enter",
        #       )
        leftvote_btn = gr.Button(
            value="👍 Upvote", visible=True, interactive=True
        )
        rightvote_btn = gr.Button(
            value="👎 Downvote", visible=True, interactive=True
        )

        callback.setup([leftvote_btn, rightvote_btn, msg, chatbot], "flagged_data_points")

        leftvote_btn.click(lambda *args: callback.flag(args), [leftvote_btn, msg, chatbot], None, preprocess=False)
        rightvote_btn.click(lambda *args: callback.flag(args), [rightvote_btn, msg, chatbot], None, preprocess=False)

        msg.submit(respond, [msg, chatbot], [msg, chatbot])
        regenerate.click(respond, [msg, chatbot], [msg, chatbot], queue=False)

    # txt.submit(add_text, [chatbot, txt], [chatbot, txt], queue=False).then(
    #         generate, inputs =[chatbot,],outputs = chatbot,)

demo.queue()
demo.launch(debug=True)

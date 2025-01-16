# import streamlit as st
# import random

# # Initialize session state
# if 'page' not in st.session_state:
#     st.session_state.page = 'Page 1'
# if 'score' not in st.session_state:
#     st.session_state.score = 0
# if 'total_questions' not in st.session_state:
#     st.session_state.total_questions = 0

# # Ion and Element Data
# elements = [
#     {'name': 'Hidrogen', 'symbol': 'H', 'group': 'IA'},
#     {'name': 'Helium', 'symbol': 'He', 'group': 'VIIIA'},
#     {'name': 'Litium', 'symbol': 'Li', 'group': 'IA'},
#     {'name': 'Karbon', 'symbol': 'C', 'group': 'IVA'},
#     {'name': 'Oksigen', 'symbol': 'O', 'group': 'VIA'},
# ]

# ions = [
#     {'name': 'Bromat', 'formula': 'BrO3-'},
#     {'name': 'Klorida', 'formula': 'Cl-'},
#     {'name': 'Nitrat', 'formula': 'NO3-'},
#     {'name': 'Sulfit', 'formula': 'SO3^2-'},
#     {'name': 'Amonium', 'formula': 'NH4+'},
# ]

# def reset_game():
#     st.session_state.score = 0
#     st.session_state.total_questions = 0

# def render_page_1():
#     st.title("Checo Games")
#     st.markdown("#")
#     st.markdown("<h1 style='text-align:center; color: pink;'>Checo Games</h1>", unsafe_allow_html=True)
#     if st.button("Start Game", key="start_game", help="Mulai Permainan"):
#         st.session_state.page = 'Page 2'

# def render_page_2():
#     st.title("Main Menu")
#     if st.button("Guess the Element", key="guess_element"):
#         st.session_state.page = 'Guess the Element'
#     if st.button("Guess the Ion", key="guess_ion"):
#         st.session_state.page = 'Guess the Ion'

# def render_guess_element():
#     st.title("Guess the Element")
#     question_types = [
#         {'type': 'name', 'question': "Yang manakah unsur {element_name}?"},
#         {'type': 'group', 'question': "Yang manakah unsur golongan {element_group}?"},
#         {'type': 'symbol', 'question': "Apa nama unsur dari simbol {element_symbol}?"}
#     ]
#     question_data = random.choice(question_types)
#     correct_element = random.choice(elements)
#     options = random.sample(elements, 4) + [correct_element]
#     random.shuffle(options)

#     if question_data['type'] == 'name':
#         question = question_data['question'].format(element_name=correct_element['name'])
#     elif question_data['type'] == 'group':
#         question = question_data['question'].format(element_group=correct_element['group'])
#     else:
#         question = question_data['question'].format(element_symbol=correct_element['symbol'])

#     st.write(question)

#     for option in options:
#         if st.button(option['name'], key=f"element_{option['name']}"):
#             if option == correct_element:
#                 st.success("Benar! Anda mendapat 10 poin.")
#                 st.session_state.score += 10
#             else:
#                 st.error("Salah! Jawaban yang benar adalah " + correct_element['name'])
#             st.session_state.total_questions += 1
#             st.experimental_rerun()

#     if st.button("Give Up", key="give_up_element"):
#         st.session_state.page = 'Page Result'


# def render_guess_ion():
#     st.title("Guess the Ion")
#     question_types = [
#         {'type': 'name', 'question': "Yang manakah ion {ion_name}?"},
#         {'type': 'formula', 'question': "Apa nama ion dari simbol {ion_formula}?"}
#     ]
#     question_data = random.choice(question_types)
#     correct_ion = random.choice(ions)
#     options = random.sample(ions, 4) + [correct_ion]
#     random.shuffle(options)

#     if question_data['type'] == 'name':
#         question = question_data['question'].format(ion_name=correct_ion['name'])
#     else:
#         question = question_data['question'].format(ion_formula=correct_ion['formula'])

#     st.write(question)

#     for option in options:
#         if st.button(option['name'], key=f"ion_{option['name']}"):
#             if option == correct_ion:
#                 st.success("Benar! Anda mendapat 10 poin.")
#                 st.session_state.score += 10
#             else:
#                 st.error("Salah! Jawaban yang benar adalah " + correct_ion['name'])
#             st.session_state.total_questions += 1
#             st.experimental_rerun()

#     if st.button("Give Up", key="give_up_ion"):
#         st.session_state.page = 'Page Result'


# def render_page_result():
#     st.title("Result")
#     if st.session_state.total_questions > 0:
#         percentage = (st.session_state.score / (st.session_state.total_questions * 10)) * 100
#     else:
#         percentage = 0
#     st.write(f"Hasil Akhir: {percentage:.2f}%")
#     st.write(f"Benar: {st.session_state.score // 10}")
#     st.write(f"Total Soal: {st.session_state.total_questions}")
#     if st.button("Menu"):
#         st.session_state.page = 'Page 1'
#         reset_game()

# # Render pages
# if st.session_state.page == 'Page 1':
#     render_page_1()
# elif st.session_state.page == 'Page 2':
#     render_page_2()
# elif st.session_state.page == 'Guess the Element':
#     render_guess_element()
# elif st.session_state.page == 'Guess the Ion':
#     render_guess_ion()
# elif st.session_state.page == 'Page Result':
#     render_page_result()

# 
# import streamlit as st
# import random

# # Initialize session state
# if 'page' not in st.session_state:
#     st.session_state.page = 'Page 1'
# if 'score' not in st.session_state:
#     st.session_state.score = 0
# if 'total_questions' not in st.session_state:
#     st.session_state.total_questions = 0

# # Ion and Element Data
# elements = [
#     {'name': 'Hidrogen', 'symbol': 'H', 'group': 'IA'},
#     {'name': 'Helium', 'symbol': 'He', 'group': 'VIIIA'},
#     {'name': 'Litium', 'symbol': 'Li', 'group': 'IA'},
#     {'name': 'Karbon', 'symbol': 'C', 'group': 'IVA'},
#     {'name': 'Oksigen', 'symbol': 'O', 'group': 'VIA'},
# ]

# ions = [
#     {'name': 'Bromat', 'formula': 'BrO3-'},
#     {'name': 'Klorida', 'formula': 'Cl-'},
#     {'name': 'Nitrat', 'formula': 'NO3-'},
#     {'name': 'Sulfit', 'formula': 'SO3^2-'},
#     {'name': 'Amonium', 'formula': 'NH4+'},
# ]

# def reset_game():
#     st.session_state.score = 0
#     st.session_state.total_questions = 0

# def render_page_1():
#     st.title("Checo Games")
#     st.markdown("#")
#     st.markdown("<h1 style='text-align:center; color: pink;'>Checo Games</h1>", unsafe_allow_html=True)
#     if st.button("Start Game", key="start_game", help="Mulai Permainan"):
#         st.session_state.page = 'Page 2'

# def render_page_2():
#     st.title("Main Menu")
#     if st.button("Guess the Element", key="guess_element"):
#         st.session_state.page = 'Guess the Element'
#     if st.button("Guess the Ion", key="guess_ion"):
#         st.session_state.page = 'Guess the Ion'

# def render_guess_element():
#     st.title("Guess the Element")
#     if 'current_question' not in st.session_state:
#         question_types = [
#             {'type': 'name', 'question': "Yang manakah unsur {element_name}?"},
#             {'type': 'group', 'question': "Yang manakah unsur golongan {element_group}?"},
#             {'type': 'symbol', 'question': "Apa nama unsur dari simbol {element_symbol}?"}
#         ]
#         question_data = random.choice(question_types)
#         correct_element = random.choice(elements)
#         options = random.sample(elements, 4) + [correct_element]
#         random.shuffle(options)

#         st.session_state.current_question = {
#             'question_data': question_data,
#             'correct_element': correct_element,
#             'options': options,
#             'answered': False
#         }

#     question_data = st.session_state.current_question['question_data']
#     correct_element = st.session_state.current_question['correct_element']
#     options = st.session_state.current_question['options']

#     if question_data['type'] == 'name':
#         question = question_data['question'].format(element_name=correct_element['name'])
#     elif question_data['type'] == 'group':
#         question = question_data['question'].format(element_group=correct_element['group'])
#     else:
#         question = question_data['question'].format(element_symbol=correct_element['symbol'])

#     st.write(question)

#     for i, option in enumerate(options):
#         if st.button(option['name'], key=f"element_{i}", disabled=st.session_state.current_question['answered']):
#             if not st.session_state.current_question['answered']:
#                 st.session_state.current_question['answered'] = True
#                 if option == correct_element:
#                     st.success("Benar! Anda mendapat 10 poin.")
#                     st.session_state.score += 10
#                 else:
#                     st.error("Salah! Jawaban yang benar adalah " + correct_element['name'])
#                 st.session_state.total_questions += 1

#     if st.session_state.current_question['answered']:
#         if st.button("Next"):
#             del st.session_state.current_question

# def render_guess_ion():
#     st.title("Guess the Ion")
#     if 'current_question_ion' not in st.session_state:
#         question_types = [
#             {'type': 'name', 'question': "Yang manakah ion {ion_name}?"},
#             {'type': 'formula', 'question': "Apa nama ion dari simbol {ion_formula}?"}
#         ]
#         question_data = random.choice(question_types)
#         correct_ion = random.choice(ions)
#         options = random.sample(ions, 4) + [correct_ion]
#         random.shuffle(options)

#         st.session_state.current_question_ion = {
#             'question_data': question_data,
#             'correct_ion': correct_ion,
#             'options': options,
#             'answered': False
#         }

#     question_data = st.session_state.current_question_ion['question_data']
#     correct_ion = st.session_state.current_question_ion['correct_ion']
#     options = st.session_state.current_question_ion['options']

#     if question_data['type'] == 'name':
#         question = question_data['question'].format(ion_name=correct_ion['name'])
#     else:
#         question = question_data['question'].format(ion_formula=correct_ion['formula'])

#     st.write(question)

#     for i, option in enumerate(options):
#         if st.button(option['name'], key=f"ion_{i}", disabled=st.session_state.current_question_ion['answered']):
#             if not st.session_state.current_question_ion['answered']:
#                 st.session_state.current_question_ion['answered'] = True
#                 if option == correct_ion:
#                     st.success("Benar! Anda mendapat 10 poin.")
#                     st.session_state.score += 10
#                 else:
#                     st.error("Salah! Jawaban yang benar adalah " + correct_ion['name'])
#                 st.session_state.total_questions += 1

#     if st.session_state.current_question_ion['answered']:
#         if st.button("Next"):
#             del st.session_state.current_question_ion

# def render_page_result():
#     st.title("Result")
#     if st.session_state.total_questions > 0:
#         percentage = (st.session_state.score / (st.session_state.total_questions * 10)) * 100
#     else:
#         percentage = 0
#     st.write(f"Hasil Akhir: {percentage:.2f}%")
#     st.write(f"Benar: {st.session_state.score // 10}")
#     st.write(f"Total Soal: {st.session_state.total_questions}")
#     if st.button("Menu"):
#         st.session_state.page = 'Page 1'
#         reset_game()

# # Render pages
# if st.session_state.page == 'Page 1':
#     render_page_1()
# elif st.session_state.page == 'Page 2':
#     render_page_2()
# elif st.session_state.page == 'Guess the Element':
#     render_guess_element()
# elif st.session_state.page == 'Guess the Ion':
#     render_guess_ion()
# elif st.session_state.page == 'Page Result':
#     render_page_result()

# import streamlit as st
# import random

# # Initialize session state
# if 'page' not in st.session_state:
#     st.session_state.page = 'Page 1'
# if 'score' not in st.session_state:
#     st.session_state.score = 0
# if 'total_questions' not in st.session_state:
#     st.session_state.total_questions = 0

# elements = [
#     {'name': 'Hidrogen', 'symbol': 'H', 'group': 'IA'},
#     {'name': 'Helium', 'symbol': 'He', 'group': 'VIIIA'},
#     {'name': 'Litium', 'symbol': 'Li', 'group': 'IA'},
#     {'name': 'Karbon', 'symbol': 'C', 'group': 'IVA'},
#     {'name': 'Oksigen', 'symbol': 'O', 'group': 'VIA'},
# ]

# ions = [
#     {'name': 'Bromat', 'formula': 'BrO3⁻'},
#     {'name': 'Klorida', 'formula': 'Cl⁻'},
#     {'name': 'Nitrat', 'formula': 'NO3⁻'},
#     {'name': 'Sulfit', 'formula': 'SO3²⁻'},
#     {'name': 'Amonium', 'formula': 'NH4⁺'},
# ]

# def reset_game():
#     st.session_state.score = 0
#     st.session_state.total_questions = 0

# def render_page_1():
#     st.markdown("<h1 style='text-align:center; color: pink;'>Checo Games</h1>", unsafe_allow_html=True)
#     if st.button("Start Game", key="start_game", help="Mulai Permainan"):
#         st.session_state.page = 'Page 2'

# def render_page_2():
#     st.title("Main Menu")
#     if st.button("Guess the Element", key="guess_element"):
#         st.session_state.page = 'Guess the Element'
#     if st.button("Guess the Ion", key="guess_ion"):
#         st.session_state.page = 'Guess the Ion'

# def render_guess_element():
#     st.title("Guess the Element")
#     if 'current_question' not in st.session_state:
#         question_types = [
#             {'type': 'name', 'question': "Yang manakah unsur {element_name}?"},
#             {'type': 'group', 'question': "Yang manakah unsur golongan {element_group}?"},
#             {'type': 'symbol', 'question': "Apa nama unsur dari simbol {element_symbol}?"}
#         ]
#         question_data = random.choice(question_types)
#         correct_element = random.choice(elements)
#         options = random.sample([e for e in elements if e != correct_element], 4) + [correct_element]
#         random.shuffle(options)

#         st.session_state.current_question = {
#             'question_data': question_data,
#             'correct_element': correct_element,
#             'options': options,
#             'answered': False
#         }

#     question_data = st.session_state.current_question['question_data']
#     correct_element = st.session_state.current_question['correct_element']
#     options = st.session_state.current_question['options']

#     if question_data['type'] == 'name':
#         question = question_data['question'].format(element_name=correct_element['name'])
#     elif question_data['type'] == 'group':
#         question = question_data['question'].format(element_group=correct_element['group'])
#     else:
#         question = question_data['question'].format(element_symbol=correct_element['symbol'])

#     st.write(question)

#     for i, option in enumerate(options):
#         display_text = option['symbol'] if question_data['type'] == 'name' else option['name']
#         if st.button(display_text, key=f"element_{i}", disabled=st.session_state.current_question['answered']):
#             if not st.session_state.current_question['answered']:
#                 st.session_state.current_question['answered'] = True
#                 if option == correct_element:
#                     st.success("Benar! Anda mendapat 10 poin.")
#                     st.session_state.score += 10
#                 else:
#                     st.error(f"Salah! Jawaban yang benar adalah {correct_element['name']} ({correct_element['symbol']}).")
#                 st.session_state.total_questions += 1

#     if st.session_state.current_question['answered']:
#         if st.button("Next"):
#             del st.session_state.current_question

#     if st.button("Give Up"):
#         st.session_state.page = 'Page Result'

# def render_guess_ion():
#     st.title("Guess the Ion")
#     if 'current_question_ion' not in st.session_state:
#         question_types = [
#             {'type': 'name', 'question': "Yang manakah ion {ion_name}?"},
#             {'type': 'formula', 'question': "Apa nama ion dari simbol {ion_formula}?"}
#         ]
#         question_data = random.choice(question_types)
#         correct_ion = random.choice(ions)
#         options = random.sample([i for i in ions if i != correct_ion], 4) + [correct_ion]
#         random.shuffle(options)

#         st.session_state.current_question_ion = {
#             'question_data': question_data,
#             'correct_ion': correct_ion,
#             'options': options,
#             'answered': False
#         }

#     question_data = st.session_state.current_question_ion['question_data']
#     correct_ion = st.session_state.current_question_ion['correct_ion']
#     options = st.session_state.current_question_ion['options']

#     if question_data['type'] == 'name':
#         question = question_data['question'].format(ion_name=correct_ion['name'])
#     else:
#         question = question_data['question'].format(ion_formula=correct_ion['formula'])

#     st.write(question)

#     for i, option in enumerate(options):
#         display_text = option['formula'] if question_data['type'] == 'name' else option['name']
#         if st.button(display_text, key=f"ion_{i}", disabled=st.session_state.current_question_ion['answered']):
#             if not st.session_state.current_question_ion['answered']:
#                 st.session_state.current_question_ion['answered'] = True
#                 if option == correct_ion:
#                     st.success("Benar! Anda mendapat 10 poin.")
#                     st.session_state.score += 10
#                 else:
#                     st.error(f"Salah! Jawaban yang benar adalah {correct_ion['name']} ({correct_ion['formula']}).")
#                 st.session_state.total_questions += 1

#     if st.session_state.current_question_ion['answered']:
#         if st.button("Next"):
#             del st.session_state.current_question_ion

#     if st.button("Give Up"):
#         st.session_state.page = 'Page Result'

# def render_page_result():
#     st.title("Result")
#     if st.session_state.total_questions > 0:
#         percentage = (st.session_state.score / (st.session_state.total_questions * 10)) * 100
#     else:
#         percentage = 0
#     st.write(f"Hasil Akhir: {percentage:.2f}%")
#     st.write(f"Benar: {st.session_state.score // 10}")
#     st.write(f"Total Soal: {st.session_state.total_questions}")
#     if st.button("Menu"):
#         st.session_state.page = 'Page 1'
#         reset_game()

# if st.session_state.page == 'Page 1':
#     render_page_1()
# elif st.session_state.page == 'Page 2':
#     render_page_2()
# elif st.session_state.page == 'Guess the Element':
#     render_guess_element()
# elif st.session_state.page == 'Guess the Ion':
#     render_guess_ion()
# elif st.session_state.page == 'Page Result':
#     render_page_result()

import streamlit as st
import random

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'Page 1'
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'total_questions' not in st.session_state:
    st.session_state.total_questions = 0

# Sample data
elements = [
    {'name': 'Hidrogen', 'symbol': 'H', 'group': 'IA'},
    {'name': 'Helium', 'symbol': 'He', 'group': 'VIIIA'},
    {'name': 'Litium', 'symbol': 'Li', 'group': 'IA'},
    {'name': 'Karbon', 'symbol': 'C', 'group': 'IVA'},
    {'name': 'Oksigen', 'symbol': 'O', 'group': 'VIA'},
]

ions = [
    {'name': 'Bromat', 'formula': 'BrO3⁻'},
    {'name': 'Klorida', 'formula': 'Cl⁻'},
    {'name': 'Nitrat', 'formula': 'NO3⁻'},
    {'name': 'Sulfit', 'formula': 'SO3²⁻'},
    {'name': 'Amonium', 'formula': 'NH4⁺'},
]

def reset_game():
    st.session_state.score = 0
    st.session_state.total_questions = 0

def render_page_1():
    st.markdown("<h1 style='text-align:center; color: pink;'>Checo Games</h1>", unsafe_allow_html=True)
    if st.button("Start Game", key="start_game", help="Mulai Permainan"):
        st.session_state.page = 'Page 2'

def render_page_2():
    st.markdown("<h2 style='text-align:center;'>Main Menu</h2>", unsafe_allow_html=True)
    if st.button("Guess the Element", key="guess_element"):
        st.session_state.page = 'Guess the Element'
    if st.button("Guess the Ion", key="guess_ion"):
        st.session_state.page = 'Guess the Ion'

def render_guess_element():
    st.markdown("<h2 style='text-align:center;'>Guess the Element</h2>", unsafe_allow_html=True)
    if 'current_question' not in st.session_state:
        question_types = [
            {'type': 'name', 'question': "Yang manakah unsur {element_name}?"},
            {'type': 'group', 'question': "Yang manakah unsur golongan {element_group}?"},
            {'type': 'symbol', 'question': "Apa nama unsur dari simbol {element_symbol}?"}
        ]
        question_data = random.choice(question_types)
        correct_element = random.choice(elements)
        options = random.sample([e for e in elements if e != correct_element], 4) + [correct_element]
        random.shuffle(options)

        st.session_state.current_question = {
            'question_data': question_data,
            'correct_element': correct_element,
            'options': options,
            'answered': False
        }

    question_data = st.session_state.current_question['question_data']
    correct_element = st.session_state.current_question['correct_element']
    options = st.session_state.current_question['options']

    if question_data['type'] == 'name':
        question = question_data['question'].format(element_name=correct_element['name'])
    elif question_data['type'] == 'group':
        question = question_data['question'].format(element_group=correct_element['group'])
    else:
        question = question_data['question'].format(element_symbol=correct_element['symbol'])

    st.write(f"<div style='text-align:center; margin-bottom:20px;'>{question}</div>", unsafe_allow_html=True)

    for i, option in enumerate(options):
        display_text = option['symbol'] if question_data['type'] == 'name' else option['name']
        if st.button(display_text, key=f"element_{i}", disabled=st.session_state.current_question['answered']):
            if not st.session_state.current_question['answered']:
                st.session_state.current_question['answered'] = True
                if option == correct_element:
                    st.success("Benar! Anda mendapat 10 poin.")
                    st.session_state.score += 10
                else:
                    st.error(f"Salah! Jawaban yang benar adalah {correct_element['name']} ({correct_element['symbol']}).")
                st.session_state.total_questions += 1

    if st.session_state.current_question['answered']:
        if st.button("Next", key="next_question", help="Lanjut ke soal berikutnya"):
            del st.session_state.current_question

    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    if st.button("Give Up", key="give_up_element"):
        st.session_state.page = 'Page Result'
    st.markdown("</div>", unsafe_allow_html=True)

def render_guess_ion():
    st.markdown("<h2 style='text-align:center;'>Guess the Ion</h2>", unsafe_allow_html=True)
    if 'current_question_ion' not in st.session_state:
        question_types = [
            {'type': 'name', 'question': "Yang manakah ion {ion_name}?"},
            {'type': 'formula', 'question': "Apa nama ion dari simbol {ion_formula}?"}
        ]
        question_data = random.choice(question_types)
        correct_ion = random.choice(ions)
        options = random.sample([i for i in ions if i != correct_ion], 4) + [correct_ion]
        random.shuffle(options)

        st.session_state.current_question_ion = {
            'question_data': question_data,
            'correct_ion': correct_ion,
            'options': options,
            'answered': False
        }

    question_data = st.session_state.current_question_ion['question_data']
    correct_ion = st.session_state.current_question_ion['correct_ion']
    options = st.session_state.current_question_ion['options']

    if question_data['type'] == 'name':
        question = question_data['question'].format(ion_name=correct_ion['name'])
    else:
        question = question_data['question'].format(ion_formula=correct_ion['formula'])

    st.write(f"<div style='text-align:center; margin-bottom:20px;'>{question}</div>", unsafe_allow_html=True)

    for i, option in enumerate(options):
        display_text = option['formula'] if question_data['type'] == 'name' else option['name']
        if st.button(display_text, key=f"ion_{i}", disabled=st.session_state.current_question_ion['answered']):
            if not st.session_state.current_question_ion['answered']:
                st.session_state.current_question_ion['answered'] = True
                if option == correct_ion:
                    st.success("Benar! Anda mendapat 10 poin.")
                    st.session_state.score += 10
                else:
                    st.error(f"Salah! Jawaban yang benar adalah {correct_ion['name']} ({correct_ion['formula']}).")
                st.session_state.total_questions += 1

    if st.session_state.current_question_ion['answered']:
        if st.button("Next", key="next_ion", help="Lanjut ke soal berikutnya"):
            del st.session_state.current_question_ion

    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    if st.button("Give Up", key="give_up_ion"):
        st.session_state.page = 'Page Result'
    st.markdown("</div>", unsafe_allow_html=True)

def render_page_result():
    st.markdown("<h2 style='text-align:center;'>Result</h2>", unsafe_allow_html=True)
    if st.session_state.total_questions > 0:
        percentage = (st.session_state.score / (st.session_state.total_questions * 10)) * 100
    else:
        percentage = 0
    st.write(f"<div style='text-align:center;'>Hasil Akhir: {percentage:.2f}%</div>", unsafe_allow_html=True)
    st.write(f"<div style='text-align:center;'>Benar: {st.session_state.score // 10}</div>", unsafe_allow_html=True)
    st.write(f"<div style='text-align:center;'>Total Soal: {st.session_state.total_questions}</div>", unsafe_allow_html=True)
    if st.button("Menu"):
        st.session_state.page = 'Page 1'
        reset_game()

if st.session_state.page == 'Page 1':
    render_page_1()
elif st.session_state.page == 'Page 2':
    render_page_2()
elif st.session_state.page == 'Guess the Element':
    render_guess_element()
elif st.session_state.page == 'Guess the Ion':
    render_guess_ion()
elif st.session_state.page == 'Page Result':
    render_page_result()

from qa_guru_8.model.pages import practice_form


def test_student_registration_form():
    practice_form.open()
    practice_form.ad_skip()

    # WHEN
    practice_form.type_name('Sasha')
    practice_form.type_surname('Sol')
    practice_form.type_email('name@example.com')
    practice_form.select_gender('Male')
    practice_form.type_phone('1234567891')
    practice_form.select_birthday('May', '1980', '11')
    practice_form.type_subjects('Computer Science')
    practice_form.select_hobby('Music')
    practice_form.type_address('Mira 1')
    practice_form.select_picture('foto.jpg')
    practice_form.select_region('NCR')
    practice_form.select_city('Delhi')
    practice_form.submit_enter()

    # THEN
    practice_form.assert_form(
            (
            'Sasha Sol',
            'name@example.com',
            'Male',
            '1234567891',
            '11 May,1980',
            'Computer Science',
            'Music',
            'foto.jpg',
            'Mira 1',
            'NCR Delhi',
            )
    )

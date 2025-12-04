from pyscript import document, display


clubs = {
    'Science Club': {'name': 'Science Club',
         'description': 'Science CLub',
         'meetingtime': 'Tuesdays (3:00pm - 4:00pm), Fridays (2:00pm - 3:00pm)',
         'location': 'Room 404',
         'moderator': 'Ms. Jameelyn Maramag',
         'membernumber': '18',
         'style': 'Academic'},
    
    'Math Club': {'name': 'Math Club',
         'description': 'Math Club',
         'meetingtime': 'Monday (2:30 PM - 4:30 PM)',
         'location': 'Room 404',
         'moderator': 'Mr. Gabuya',
         'membernumber': '16',
         'style': 'Academic'},

    'Marching Band': {'name': 'Marching Band',
         'description': 'Marching Band',
         'meetingtime': 'Monday, Tuesday and Wednesday (3:00 - 4:30)',
         'location': 'Marching Band Room ',
         'moderator': 'Mr. Emilio Alumno',
         'membernumber': '42',
         'style': 'Non-Academic'},

    'Glee Club': {'name': 'Glee Club',
         'description': 'Glee Club',
         'meetingtime': 'Monday & Friday 3:00-4:30 PM',
         'location': 'HS Music Room',
         'moderator': 'Sir. Denver Martin',
         'membernumber': '28',
         'style': 'Non-Academic'},
    
    'Basketball Varsity': {'name': 'Basketball Varsity',
         'description': 'Basketball Varsity',
         'meetingtime': 'Monday (3:00pm - 5pm',
         'location': 'Quadrangle',
         'moderator': 'Mr. Adrian Ruiz',
         'membernumber': '16',
         'style': 'Non-Academic'},

    'Volleyball Varsity': {'name': 'Volleyball Varsity',
         'description': 'Volleyball Varsity',
         'meetingtime': 'Wednesday (3:00 - 4:00)',
         'location': 'Quadrangle',
         'moderator': 'Mr. Adrian Ruiz',
         'membernumber': '23',
         'style': 'Non-Academic'}
} #DICTIONARY VARIABLE THAT CONTAINS ALL THE CLUBS

def show_club_info(e): #SHOWS WHAT CLUB IS SELECTED AND ITS INFORMATION
    selected_club = document.getElementById('club-dropdown').value #GETS SELECTED CLUB FROM THE DROPDOWN MENU
    club_info = clubs.get(selected_club, {}) #GETS THE INFORMATION OF THE SELECTED CLUB FROM THE DICTIONARY
    
    if club_info: #IF THE CLUB INFO EXISTS
        info_display = f"""
        Club Name: {club_info.get('name')}
        Club Description: {club_info.get('description')}
        Club Meeting Time: {club_info.get('meetingtime')}
        Club Location: {club_info.get('location')}
        Club Mentor: {club_info.get('moderator')}
        Club Number of Members: {club_info.get('membernumber')}
        Club Category: {club_info.get('style')}
        """
    else:
        info_display = "Club information not found."
    
    display(info_display, target='club-details')
# from django.shortcuts import render
#
# theme = ['Python Basics',
#           'Django Introduction',
#           'Django Models',
#           'Django Views',
#           'Django Templates',
#           'Django Forms',
#           'Django Admin']
#
#
# def theme_list(request):
#     return render(request, template_name='tema.html', context={'themes': theme})


from django.shortcuts import render

def theme_list(request):
    with open('lessons.txt', 'r') as file:
        themes = file.readlines()
    context = {
        'themes': themes,
    }
    return render(request, 'themes/theme_list.html', context)


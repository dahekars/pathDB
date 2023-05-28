from django.shortcuts import render
import subprocess

def search(request):
    query = request.GET.get('q')
    # Perform the search logic here
    results = []  # Placeholder for search results
    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'search.html', context)
import subprocess

def check_remote_system_status(remote_host):
    # Run the ping command with a single packet and a timeout of 1 second
    result = subprocess.run(['ping', '-c', '1', '-W', '1', remote_host], capture_output=True)
    
    if result.returncode == 0:
        return True  # Remote system is reachable
    else:
        return False  # Remote system is not reachable


def home(request):
    query = request.GET.get('q', '')
    results = []  # Placeholder for search results
    
    if query:
        # Perform the search logic here based on the query
        # Assign the search results to the 'results' variable

        context = {
        'query': query,
        'results': results,
        }
    
    interviewuser_01 = 'example.com'  # Replace with the IP or domain name of the remote system
    interviewuser_02 = 'example.com'  # Replace with the IP or domain name of the remote system
    interviewuser_03 = 'example.com'  # Replace with the IP or domain name of the remote system
    interviewuser_04 = 'example.com'  # Replace with the IP or domain name of the remote system
    interviewuser_05 = 'example.com'  # Replace with the IP or domain name of the remote system
    interviewuser_06 = 'example.com'  # Replace with the IP or domain name of the remote system
    interviewuser_07 = 'example.com'  # Replace with the IP or domain name of the remote system
    interviewuser_08 = 'example.com'  # Replace with the IP or domain name of the remote system
    interviewuser_09 = 'example.com'  # Replace with the IP or domain name of the remote system
    interviewuser_10 = 'example.com'  # Replace with the IP or domain name of the remote system
    hnjlicsrv01 = 'example.com'  # Replace with the IP or domain name of the remote system
    hnjlicsrv02 = 'example.com'  # Replace with the IP or domain name of the remote system
    hnjlicsrv03 = 'example.com'  # Replace with the IP or domain name of the remote system
    interviewuser_ = 'example.com'  # Replace with the IP or domain name of the remote system
    interviewuser_ = 'example.com'  # Replace with the IP or domain name of the remote system
    interviewuser_ = 'example.com'  # Replace with the IP or domain name of the remote system
    interviewuser_ = 'example.com'  # Replace with the IP or domain name of the remote system
    
    interviewuser_01_status = check_remote_system_status(interviewuser_01)
    interviewuser_02_status = check_remote_system_status(interviewuser_02)
    interviewuser_03_status = check_remote_system_status(interviewuser_03)
    interviewuser_04_status = check_remote_system_status(interviewuser_04)
    interviewuser_05_status = check_remote_system_status(interviewuser_05)
    interviewuser_06_status = check_remote_system_status(interviewuser_06)
    interviewuser_07_status = check_remote_system_status(interviewuser_07)
    interviewuser_08_status = check_remote_system_status(interviewuser_08)
    interviewuser_09_status = check_remote_system_status(interviewuser_09)
    interviewuser_10_status = check_remote_system_status(interviewuser_10)
    hnjlicsrv01_status = check_remote_system_status(hnjlicsrv01)
    hnjlicsrv02_status = check_remote_system_status(hnjlicsrv02)
    hnjlicsrv03_status = check_remote_system_status(hnjlicsrv03)
    interviewuser__status = check_remote_system_status(interviewuser_)
    interviewuser__status = check_remote_system_status(interviewuser_)
    interviewuser__status = check_remote_system_status(interviewuser_)
    interviewuser__status = check_remote_system_status(interviewuser_)

    context = {
        'interviewuser_01': interviewuser_01_status,
        'interviewuser_02': interviewuser_02_status,
        'interviewuser_03': interviewuser_03_status,
        'interviewuser_04': interviewuser_04_status,
        'interviewuser_05': interviewuser_05_status,
        'interviewuser_06': interviewuser_06_status,
        'interviewuser_07': interviewuser_07_status,
        'interviewuser_08': interviewuser_08_status,
        'interviewuser_09': interviewuser_09_status,
        'interviewuser_10': interviewuser_10_status,
        'hnjlicsrv01': hnjlicsrv01_status,
        'hnjlicsrv02': hnjlicsrv02_status,
        'hnjlicsrv03': hnjlicsrv03_status,
        'interviewuser_': interviewuser__status,
        'interviewuser_': interviewuser__status,
        'interviewuser_': interviewuser__status,
        'interviewuser_': interviewuser__status,
    }
    return render(request, 'home.html', context)
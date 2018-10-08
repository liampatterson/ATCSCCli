import click
import requests

__author__ = "Liam Patterson"

def main():
	"""
	Simple CLI to grab the current ATCSCC status from the FAA via HTML
	"""
	pass

@main.command()
@click.argument('delays')

def get(delays):
	"""Returns US Airport Delays and Summary"""
	url_format = 'https://soa.smext.faa.gov/asws/api/airport/delays'
	response = requests.get( url_format )
	
	groundStops = ( response.json()['GroundStops'] ).values()
	groundDelays = ( response.json()['GroundDelays'] ).values()
	closures = ( response.json()['Closures'] ).values()
	arriveDepartDelays = ( response.json()['ArriveDepartDelays'] ).values()
	

if __name__ == "__main__":
	main()


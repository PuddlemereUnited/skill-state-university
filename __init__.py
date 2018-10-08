# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
import requests


API_URL = 'http://universities.hipolabs.com/'
SEARCH = API_URL + 'search'

def search_university(state_name):
    parameters = {"name": state_name, "country": 'united states'}
    r = requests.get(SEARCH, params=parameters)

    if (200 <= r.status_code < 300):
        data = r.json()
        university_names = [li['name'] for li in data]
        return university_names
    else:
        return None



# TODO: Change "Template" to a unique name for your skill
class StateUniversitySkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(StateUniversitySkill, self).__init__(name="StateUniversitySkill")

    @intent_file_handler('State.intent')
    def get_state_university(self, message):
        list_university = search_cocktail('oklahoma')
        if list_university:
            self.speak_dialog(message.data['state'])
            '''
             self.speak_dialog("SateUniversity", {
                                  'state': 'oklahoma',
                                  'university': list_university})           
            '''
        else:
            self.speak_dialog('NotFound')

    #   'Greetings planet earth'
    @intent_handler(IntentBuilder("").require("State").require("University"))
    def handle_hello_world_intent(self, message):
        # In this case, respond by simply speaking a canned response.
        # Mycroft will randomly speak one of the lines from the file
        #    dialogs/en-us/hello.world.dialog
        self.speak_dialog("state.university")


    # def stop(self):
    #    return False

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return StateUniversitySkill()

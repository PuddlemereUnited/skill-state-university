# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
#from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft import MycroftSkill, intent_file_handler, intent_handler, AdaptIntent
from mycroft.util.log import LOG
import json

def search_manual(situation):
    with open('troubleshoot.json') as f:
        data = json.load(f)

    situation_names = [li['name'] == situation for li in data]
    return situation_names



class UserManualSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(UserManualSkill, self).__init__(name="UserManualSkill")

    @intent_file_handler('troubleshoot.intent')
    def get_state_university(self, message):
        list_CommonCauses = search_manual(message.data['situation'])
        #list_university = True

        if list_CommonCauses:
            #self.speak_dialog("SateUniversity", {'state': 'oklahoma', 'university': list_university})
            self.speak_dialog("TroubleShoot", {'situation': message.data['situation'], 'commonCause': list_CommonCauses})

        else:
            self.speak_dialog('NotFound')

    #   'Greetings planet earth'
    @intent_handler(IntentBuilder("").require("CompressorRotation"))
    def handle_compressor_rotation(self, message):
        # Mycroft will randomly speak one of the lines from the file
        #    dialogs/en-us/hello.world.dialog  
        list_CommonCauses = search_manual("Compressor")
        self.speak_dialog("TroubleShoot", {'situation': 'Compressor will not rotate', 'commonCuase': list_CommonCauses})

    @intent_handler(IntentBuilder("").require("temperature"))
    def handle_compressor_temperature(self, message):
        # Mycroft will randomly speak one of the lines from the file
        #    dialogs/en-us/hello.world.dialog  
        list_CommonCauses = search_manual("Temperature")
        self.speak_dialog("TroubleShoot", {'situation': 'Temperature', 'commonCuase': list_CommonCauses})


    # def stop(self):
    #    return False

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return UserManualSkill()



import json
situation = "Temperature"
with open('troubleshoot.json') as f:
    data = json.load(f)

situation_names = [li['name'] == situation for li in data]
return situation_names
from GetSaramIn import Call_Saramin_Pages
from JobKorea import Get_JobKorea_Pages
from Save import save_to_file

SaramInJob = Call_Saramin_Pages()

JobKoreaJob = Get_JobKorea_Pages()

jobs = SaramInJob+JobKoreaJob

# save_to_file(jobs)

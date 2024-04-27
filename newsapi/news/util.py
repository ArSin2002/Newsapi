from datetime import datetime

parameter_called_time = {}


def is_api_call_required(parameter, time=600):
    consolidated_parameters = "".join(parameter.values())
    curr_time = datetime.now()
    if consolidated_parameters in parameter_called_time:
        prev_time = parameter_called_time[consolidated_parameters]
        time_diff = curr_time - prev_time

        if time_diff.total_seconds() > time:
            parameter_called_time[consolidated_parameters] = curr_time
            return True
        return False
    parameter_called_time[consolidated_parameters] = curr_time
    return True

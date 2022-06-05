SimeonFriendlyName = 'Simeon Test Tracker'
SimeonEntityPicture = '/local/icons/Simeon.png'
SimeontrackerName = 'device_tracker.test_simeon'

ClaireFriendlyName = 'Claire Test Tracker'
ClaireEntityPicture = '/local/icons/Claire.png'
ClairetrackerName = 'device_tracker.test_claire'

SimeoncurrentState = hass.states.get(SimeontrackerName)
SimeonnewStatus = SimeoncurrentState.state

ClairecurrentState = hass.states.get(ClairetrackerName)
ClairenewStatus = ClairecurrentState.state

# Create device_tracker.test_simeon entity
hass.states.set(SimeontrackerName, SimeonnewStatus, {
    'friendly_name': SimeonFriendlyName,
    'entity_picture': SimeonEntityPicture,
    'show_last_changed': 'true'
})

# Create device_tracker.test_claire entity
hass.states.set(ClairetrackerName, ClairenewStatus, {
    'friendly_name': ClaireFriendlyName,
    'entity_picture': ClaireEntityPicture,
    'show_last_changed': 'true'
})
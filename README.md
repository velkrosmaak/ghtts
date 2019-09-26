# Google Home TTS webhook

The problem I was solving with this is that my Home Assistant VM's network config means the HASS native TTS doesn't play any audio on my Google Home devices.

The solution was to move that functionality onto another VM. A quick Google revealed this excellent library [https://pypi.org/project/googlehomepush/] which takes care of the TTS side, I just had to make it easily accessible from HASS.

To do that, I used Flask to create a quick, cheap and dirty webserver on port 8069 because I like that port. Supply a parameter to the /say endpoint and this will be passed to the GoogleHomePush library which will result in the Google lady speaking the text.

Since this is just a URL you can call, you can use this wherever that's possible, in order to add automated speech to your home.

My HASS config looks as follows:

### configuration.yaml
```
shell_command:
say_stuff: 'curl -G http://box_this_is_running_on:8069/say/ --data-urlencode "saywhat={{ speech_text }}"'
```

### old_automations.yaml
```
- service: shell_command.say_stuff
  data_template:
      speech_text: "It is {{states('sensor.living_room_temperature')}} degrees in the living room."
```

This can then be invoked like so:

```
curl -G http://localhost:8069/say/ --data-urlencode "saywhat=Lou Reed is great!"
```

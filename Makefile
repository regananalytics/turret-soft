.PHONY: all

clean:
	find . | grep -E "__pycache__" | xargs rm -rf
	find . | grep -E ".egg-info" | xargs rm -rf


build:
	docker build ./turret-soft/turret_soft/docker/ -t danregan/turret_soft:latest

push:
	docker push danregan/turret_soft:latest


run:
	export AUDIO_GROUP=${getent group audio | cut -d: -f3}
	docker run \
	--device /dev/snd \
	-e PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native \
	-v ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native \
	-v ~/.config/pulse/cookie:/root/.config/pulse/cookie \
	--group-add ${AUDIO_GROUP} \
	turret_soft:latest

deploy:
	REMOTE=turret
	docker -H "ssh://$(REMOTE)" run \
		--device /dev/snd \
		-e PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native \
		-v ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native \
		-v ~/.config/pulse/cookie:/root/.config/pulse/cookie \
		--group-add $(getent group audio | cut -d: -f3) \
		turret_soft:latest
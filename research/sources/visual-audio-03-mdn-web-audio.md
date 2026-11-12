Source: https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API
Title: Web Audio API - Web APIs | MDN
Fetched: 2026-11-12T03:01:14.090Z

- [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API#content)
- [Skip to search](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API#mdn-search)

Learn frontend, backend, and AI from our course partner
[Scrimba](https://scrimba.com/learn/frontend?via=mdn)

# Web Audio API

Baseline


Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2021.

\\* Some parts of this feature may have varying levels of support.


- [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API#browser_compatibility)
- [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)

The Web Audio API provides a powerful and versatile system for controlling audio on the Web, allowing developers to choose audio sources, add effects to audio, create audio visualizations, apply spatial effects (such as panning) and much more.

## [Web audio concepts and usage](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API\#web_audio_concepts_and_usage)

The Web Audio API involves handling audio operations inside an **audio context**, and has been designed to allow **modular routing**. Basic audio operations are performed with **audio nodes**, which are linked together to form an **audio routing graph**. Several sources — with different types of channel layout — are supported even within a single context. This modular design provides the flexibility to create complex audio functions with dynamic effects.

Audio nodes are linked into chains and simple webs by their inputs and outputs. They typically start with one or more sources. Sources provide arrays of samples — measurements of the audio signal's amplitude at successive moments in time — often tens of thousands per second. These could be either computed mathematically (such as [`OscillatorNode`](https://developer.mozilla.org/en-US/docs/Web/API/OscillatorNode)), or they can be recordings from sound/video files (like [`AudioBufferSourceNode`](https://developer.mozilla.org/en-US/docs/Web/API/AudioBufferSourceNode) and [`MediaElementAudioSourceNode`](https://developer.mozilla.org/en-US/docs/Web/API/MediaElementAudioSourceNode)) and audio streams ( [`MediaStreamAudioSourceNode`](https://developer.mozilla.org/en-US/docs/Web/API/MediaStreamAudioSourceNode)). In fact, sound files are just recordings of sound intensities themselves, which come in from microphones or electric instruments, and get mixed down into a single, complicated wave.

Outputs of these nodes could be linked to inputs of others, which mix or modify these streams of sound samples into different streams. A common modification is multiplying the samples by a value to make them louder or quieter (as is the case with [`GainNode`](https://developer.mozilla.org/en-US/docs/Web/API/GainNode)). Once the sound has been sufficiently processed for the intended effect, it can be linked to the input of a destination ( [`BaseAudioContext.destination`](https://developer.mozilla.org/en-US/docs/Web/API/BaseAudioContext/destination)), which sends the sound to the speakers or headphones. This last connection is only necessary if the user is supposed to hear the audio.

A simple, typical workflow for web audio would look something like this:

1. Create audio context
2. Inside the context, create sources — such as `<audio>`, oscillator, stream
3. Create effects nodes, such as reverb, biquad filter, panner, compressor
4. Choose final destination of audio, for example your system speakers
5. Connect the sources up to the effects, and the effects to the destination.

![A simple box diagram with an outer box labeled Audio context, and three inner boxes labeled Sources, Effects and Destination. The three inner boxes have arrows between them pointing from left to right, indicating the flow of audio information.](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/audio-context_.png)

Timing is controlled with high precision and low latency, allowing developers to write code that responds accurately to events and is able to target specific samples, even at a high sample rate. So applications such as drum machines and sequencers are well within reach.

The Web Audio API also allows us to control how audio is _spatialized_. Using a system based on a _source-listener model_, it allows control of the _panning model_ and deals with _distance-induced attenuation_ induced by a moving source (or moving listener).

**Note:**
You can read about the theory of the Web Audio API in a lot more detail in our article [Basic concepts behind Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Basic_concepts_behind_Web_Audio_API).

## [Web Audio API target audience](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API\#web_audio_api_target_audience)

The Web Audio API can seem intimidating to those that aren't familiar with audio or music terms, and as it incorporates a great deal of functionality it can prove difficult to get started if you are a developer.

It can be used to incorporate audio into your website or application, by [providing atmosphere like futurelibrary.no](https://www.futurelibrary.no/ "External link (opens in new tab)"), or [auditory feedback on forms](https://css-tricks.com/form-validation-web-audio/ "External link (opens in new tab)"). However, it can also be used to create _advanced_ interactive instruments. With that in mind, it is suitable for both developers and musicians alike.

We have a [simple introductory tutorial](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API) for those that are familiar with programming but need a good introduction to some of the terms and structure of the API.

There's also a [Basic Concepts Behind Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Basic_concepts_behind_Web_Audio_API) article, to help you understand the way digital audio works, specifically in the realm of the API. This also includes a good introduction to some of the concepts the API is built upon.

Learning coding is like playing cards — you learn the rules, then you play, then you go back and learn the rules again, then you play again. So if some of the theory doesn't quite fit after the first tutorial and article, there's an [advanced tutorial](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Advanced_techniques) which extends the first one to help you practice what you've learned, and apply some more advanced techniques to build up a step sequencer.

We also have other tutorials and comprehensive reference material available that covers all features of the API. See the sidebar on this page for more.

If you are more familiar with the musical side of things, are familiar with music theory concepts, want to start building instruments, then you can go ahead and start building things with the advanced tutorial and others as a guide (the above-linked tutorial covers scheduling notes, creating bespoke oscillators and envelopes, as well as an LFO among other things.)

If you aren't familiar with the programming basics, you might want to consult some beginner's JavaScript tutorials first and then come back here — see our [Beginner's JavaScript learning module](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting) for a great place to begin.

## [Web Audio API interfaces](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API\#web_audio_api_interfaces)

The Web Audio API has a number of interfaces and associated events, which we have split up into nine categories of functionality.

### [General audio graph definition](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API\#general_audio_graph_definition)

General containers and definitions that shape audio graphs in Web Audio API usage.

[`AudioContext`](https://developer.mozilla.org/en-US/docs/Web/API/AudioContext)

The **`AudioContext`** interface represents an audio-processing graph built from audio modules linked together, each represented by an [`AudioNode`](https://developer.mozilla.org/en-US/docs/Web/API/AudioNode). An audio context controls the creation of the nodes it contains and the execution of the audio processing, or decoding. You need to create an `AudioContext` before you do anything else, as everything happens inside a context.

[`AudioNode`](https://developer.mozilla.org/en-US/docs/Web/API/AudioNode)

The **`AudioNode`** interface represents an audio-processing module like an _audio source_ (e.g., an HTML [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio) or [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video) element), _audio destination_, _intermediate processing module_ (e.g., a filter like [`BiquadFilterNode`](https://developer.mozilla.org/en-US/docs/Web/API/BiquadFilterNode), or _volume control_ like [`GainNode`](https://developer.mozilla.org/en-US/docs/Web/API/GainNode)).

[`AudioParam`](https://developer.mozilla.org/en-US/docs/Web/API/AudioParam)

The **`AudioParam`** interface represents an audio-related parameter, like one of an [`AudioNode`](https://developer.mozilla.org/en-US/docs/Web/API/AudioNode). It can be set to a specific value or a change in value, and can be scheduled to happen at a specific time and following a specific pattern.

[`AudioParamMap`](https://developer.mozilla.org/en-US/docs/Web/API/AudioParamMap)

Provides a map-like interface to a group of [`AudioParam`](https://developer.mozilla.org/en-US/docs/Web/API/AudioParam) interfaces, which means it provides the methods `forEach()`, `get()`, `has()`, `keys()`, and `values()`, as well as a `size` property.

[`BaseAudioContext`](https://developer.mozilla.org/en-US/docs/Web/API/BaseAudioContext)

The **`BaseAudioContext`** interface acts as a base definition for online and offline audio-processing graphs, as represented by [`AudioContext`](https://developer.mozilla.org/en-US/docs/Web/API/AudioContext) and [`OfflineAudioContext`](https://developer.mozilla.org/en-US/docs/Web/API/OfflineAudioContext) respectively. You wouldn't use `BaseAudioContext` directly — you'd use its features via one of these two inheriting interfaces.

The [`ended`](https://developer.mozilla.org/en-US/docs/Web/API/AudioScheduledSourceNode/ended_event "ended") event

The `ended` event is fired when playback has stopped because the end of the media was reached.

### [Defining audio sources](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API\#defining_audio_sources)

Interfaces that define audio sources for use in the Web Audio API.

[`AudioScheduledSourceNode`](https://developer.mozilla.org/en-US/docs/Web/API/AudioScheduledSourceNode)

The **`AudioScheduledSourceNode`** is a parent interface for several types of audio source node interfaces. It is an [`AudioNode`](https://developer.mozilla.org/en-US/docs/Web/API/AudioNode).

[`OscillatorNode`](https://developer.mozilla.org/en-US/docs/Web/API/OscillatorNode)

The **`OscillatorNode`** interface represents a periodic waveform, which can be sine, square, sawtooth, triangle, or custom. It is an [`AudioNode`](https://developer.mozilla.org/en-US/docs/Web/API/AudioNode) audio-processing module that causes a given _frequency_ of wave to be created.

[`AudioBuffer`](https://developer.mozilla.org/en-US/docs/Web/API/AudioBuffer)

The **`AudioBuffer`** interface represents a short audio asset residing in memory, created from an audio file using the [`BaseAudioContext.decodeAudioData`](https://developer.mozilla.org/en-US/docs/Web/API/BaseAudioContext/decodeAudioData) method, or created with raw data using [`BaseAudioContext.createBuffer`](https://developer.mozilla.org/en-US/docs/Web/API/BaseAudioContext/createBuffer). Once decoded into this form, the audio can then be put into an [`AudioBufferSourceNode`](https://developer.mozilla.org/en-US/docs/Web/API/AudioBufferSourceNode).

[`AudioBufferSourceNode`](https://developer.mozilla.org/en-US/docs/Web/API/AudioBufferSourceNode)

The **`AudioBufferSourceNode`** interface represents an audio source consisting of in-memory audio data, stored in an [`AudioBuffer`](https://developer.mozilla.org/en-US/docs/Web/API/AudioBuffer). It is an [`AudioNode`](https://developer.mozilla.org/en-US/docs/Web/API/AudioNode) that acts as an audio source.

[`MediaElementAudioSourceNode`](https://developer.mozilla.org/en-US/docs/Web/API/MediaElementAudioSourceNode)

The **`MediaElementAudioSourceNode`** interface represents an audio source consisting of an HTML [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio) or [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video) element. It is an [`AudioNode`](https://developer.mozilla.org/en-US/docs/Web/API/AudioNode) that acts as an audio source.

[`MediaStreamAudioSourceNode`](https://developer.mozilla.org/en-US/docs/Web/API/MediaStreamAudioSourceNode)

The **`MediaStreamAudioSourceNode`** interface represents an audio source consisting of a [`MediaStream`](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream) (such as a webcam, microphone, or a stream being sent from a remote computer). If multiple audio tracks are present on the stream, the track whose [`id`](https://developer.mozilla.org/en-US/docs/Web/API/MediaStreamTrack/id "id") comes first lexicographically (alphabetically) is used. It is an [`AudioNode`](https://developer.mozilla.org/en-US/docs/Web/API/AudioNode) that acts as an audio source.

[`MediaStreamTrackAudioSourceNode`](https://developer.mozilla.org/en-US/docs/Web/API/MediaStreamTrackAudioSourceNode)

A node of type [`MediaStreamTrackAudioSourceNode`](https://developer.mozilla.org/en-US/docs/Web/API/MediaStreamTrackAudioSourceNode) represents an audio source whose data comes from a [`MediaStreamTrack`](https://developer.mozilla.org/en-US/docs/Web/API/MediaStreamTrack). When creating the node using the [`createMediaStreamTrackSource()`](https://developer.mozilla.org/en-US/docs/Web/API/AudioContext/createMediaStreamTrackSource "createMediaStreamTrackSource()") method to create the node, you specify which track to use. This provides more control than `MediaStreamAudioSourceNode`.

### [Defining audio effects filters](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API\#defining_audio_effects_filters)

Interfaces for defining effects that you want to apply to your audio sources.

[`BiquadFilterNode`](https://developer.mozilla.org/en-US/docs/Web/API/BiquadFilterNode)

The **`BiquadFilterNode`** interface represents a simple low-order filter. It is an [`AudioNode`](https://developer.mozilla.org/en-US/docs/Web/API/AudioNode) that can represent different kinds of filters, tone control devices, or graphic equalizers. A `BiquadFilterNode` always has exactly one input and one output.

[`ConvolverNode`](https://developer.mozilla.org/en-US/docs/Web/API/ConvolverNode)

The **`ConvolverNode`** interface is an [`AudioNode`](https://developer.mozilla.org/en-US/docs/Web/API/AudioNode) that performs a Linear Convolution on a given [`AudioBuffer`](https://developer.mozilla.org/en-US/docs/Web/API/AudioBuffer), and is often used to achieve a reverb effect.

[`DelayNode`](https://developer.mozilla.org/en-US/docs/Web/API/DelayNode)

The **`DelayNode`** interface represents a [delay-line](https://en.wikipedia.org/wiki/Digital_delay_line "External link (opens in new tab)"); an [`AudioNode`](https://developer.mozilla.org/en-US/docs/Web/API/AudioNode) audio-processing module that causes a delay between the arrival of an input data and its propagation to the output.

[`DynamicsCompressorNode`](https://developer.mozilla.org/en-US/docs/Web/API/DynamicsCompressorNode)

The **`DynamicsCompressorNode`** interface provides a compression effect, which lowers the volume of the loudest parts of the signal in order to help prevent clipping and distortion that can occur when multiple sounds are played and multiplexed together at once.

[`GainNode`](https://developer.mozilla.org/en-US/docs/Web/API/GainNode)

The **`GainNode`** interface represents a change in volume. It is an [`AudioNode`](https://developer.mozilla.org/en-US/docs/Web/API/AudioNode) audio-processing module that causes a given _gain_ to be applied to the input data before its propagation to the output.

[`WaveShaperNode`](https://developer.mozilla.org/en-US/docs/Web/API/WaveShaperNode)

The **`WaveShaperNode`** interface represents a non-linear distorter. It is an [`AudioNode`](https://developer.mozilla.org/en-US/docs/Web/API/AudioNode) that use a curve to apply a waveshaping distortion to the signal. Beside obvious distortion effects, it is often used to add a warm feeling to the signal.

[`PeriodicWave`](https://developer.mozilla.org/en-US/docs/Web/API/PeriodicWave)

Describes a periodic waveform that can be used to shape the output of an [`OscillatorNode`](https://developer.mozilla.org/en-US/docs/Web/API/OscillatorNode).

[`IIRFilterNode`](https://developer.mozilla.org/en-US/docs/Web/API/IIRFilterNode)

Implements a general [infinite impulse response](https://en.wikipedia.org/wiki/Infinite_impulse_response "External link (opens in new tab)") (IIR) filter; this type of filter can be used to implement tone-control devices and graphic equalizers as well.

### [Defining audio destinations](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API\#defining_audio_destinations)

Once you are done processing your audio, these interfaces define where to output it.

[`AudioDestinationNode`](https://developer.mozilla.org/en-US/docs/Web/API/AudioDestinationNode)

The **`AudioDestinationNode`** interface represents the end destination of an audio source in a given context — usually the speakers of your device.

[`MediaStreamAudioDestinationNode`](https://developer.mozilla.org/en-US/docs/Web/API/MediaStreamAudioDestinationNode)

The **`MediaStreamAudioDestinationNode`** interface represents an audio destination consisting of a [WebRTC](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API) [`MediaStream`](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream) with a single `AudioMediaStreamTrack`, which can be used in a similar way to a [`MediaStream`](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream) obtained from [`getUserMedia()`](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia "getUserMedia()"). It is an [`AudioNode`](https://developer.mozilla.org/en-US/docs/Web/API/AudioNode) that acts as an audio destination.

### [Data analysis and visualization](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API\#data_analysis_and_visualization)

Interfaces for extracting audio graph statistics, for the purposes of data analysis and visualization.

[`AnalyserNode`](https://developer.mozilla.org/en-US/docs/Web/API/AnalyserNode)

Represents a node able to provide real-time frequency and time-domain analysis information.

[`AudioPlaybackStats`](https://developer.mozilla.org/en-US/docs/Web/API/AudioPlaybackStats)

Provides access to duration, underrun, and latency statistics for the associated [`AudioContext`](https://developer.mozilla.org/en-US/docs/Web/API/AudioContext). These statistics allow you to measure audio delay and glitches.

### [Splitting and merging audio channels](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API\#splitting_and_merging_audio_channels)

To split and merge audio channels, you'll use these interfaces.

[`ChannelSplitterNode`](https://developer.mozilla.org/en-US/docs/Web/API/ChannelSplitterNode)

The **`ChannelSplitterNode`** interface separates the different channels of an audio source out into a set of _mono_ outputs.

[`ChannelMergerNode`](https://developer.mozilla.org/en-US/docs/Web/API/ChannelMergerNode)

The **`ChannelMergerNode`** interface reunites different mono inputs into a single output. Each input will be used to fill a channel of the output.

### [Audio spatialization](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API\#audio_spatialization)

These interfaces allow you to add audio spatialization panning effects to your audio sources.

[`AudioListener`](https://developer.mozilla.org/en-US/docs/Web/API/AudioListener)

The **`AudioListener`** interface represents the position and orientation of the unique person listening to the audio scene used in audio spatialization.

[`PannerNode`](https://developer.mozilla.org/en-US/docs/Web/API/PannerNode)

The **`PannerNode`** interface represents the position and behavior of an audio source signal in 3D space, allowing you to create complex panning effects.

[`StereoPannerNode`](https://developer.mozilla.org/en-US/docs/Web/API/StereoPannerNode)

The **`StereoPannerNode`** interface represents a simple stereo panner node that can be used to pan an audio stream left or right.

### [Audio processing in JavaScript](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API\#audio_processing_in_javascript)

Using audio worklets, you can define custom audio nodes written in JavaScript or [WebAssembly](https://developer.mozilla.org/en-US/docs/WebAssembly). Audio worklets implement the [`Worklet`](https://developer.mozilla.org/en-US/docs/Web/API/Worklet) interface, a lightweight version of the [`Worker`](https://developer.mozilla.org/en-US/docs/Web/API/Worker) interface.

[`AudioWorklet`](https://developer.mozilla.org/en-US/docs/Web/API/AudioWorklet)

The `AudioWorklet` interface is available through the [`AudioContext`](https://developer.mozilla.org/en-US/docs/Web/API/AudioContext) object's [`audioWorklet`](https://developer.mozilla.org/en-US/docs/Web/API/BaseAudioContext/audioWorklet "audioWorklet"), and lets you add modules to the audio worklet to be executed off the main thread.

[`AudioWorkletNode`](https://developer.mozilla.org/en-US/docs/Web/API/AudioWorkletNode)

The `AudioWorkletNode` interface represents an [`AudioNode`](https://developer.mozilla.org/en-US/docs/Web/API/AudioNode) that is embedded into an audio graph and can pass messages to the corresponding `AudioWorkletProcessor`.

[`AudioWorkletProcessor`](https://developer.mozilla.org/en-US/docs/Web/API/AudioWorkletProcessor)

The `AudioWorkletProcessor` interface represents audio processing code running in an `AudioWorkletGlobalScope` that generates, processes, or analyzes audio directly, and can pass messages to the corresponding `AudioWorkletNode`.

[`AudioWorkletGlobalScope`](https://developer.mozilla.org/en-US/docs/Web/API/AudioWorkletGlobalScope)

The `AudioWorkletGlobalScope` interface is a `WorkletGlobalScope`-derived object representing a worker context in which an audio processing script is run; it is designed to enable the generation, processing, and analysis of audio data directly using JavaScript in a worklet thread rather than on the main thread.

#### Obsolete: script processor nodes

Before audio worklets were defined, the Web Audio API used the `ScriptProcessorNode` for JavaScript-based audio processing. Because the code runs in the main thread, they have bad performance. The `ScriptProcessorNode` is kept for historic reasons but is marked as deprecated.

[`ScriptProcessorNode`](https://developer.mozilla.org/en-US/docs/Web/API/ScriptProcessorNode)

The **`ScriptProcessorNode`** interface allows the generation, processing, or analyzing of audio using JavaScript. It is an [`AudioNode`](https://developer.mozilla.org/en-US/docs/Web/API/AudioNode) audio-processing module that is linked to two buffers, one containing the current input, one containing the output. An event, implementing the [`AudioProcessingEvent`](https://developer.mozilla.org/en-US/docs/Web/API/AudioProcessingEvent) interface, is sent to the object each time the input buffer contains new data, and the event handler terminates when it has filled the output buffer with data.

[`audioprocess`](https://developer.mozilla.org/en-US/docs/Web/API/ScriptProcessorNode/audioprocess_event "audioprocess") (event)

The `audioprocess` event is fired when an input buffer of a Web Audio API [`ScriptProcessorNode`](https://developer.mozilla.org/en-US/docs/Web/API/ScriptProcessorNode) is ready to be processed.

[`AudioProcessingEvent`](https://developer.mozilla.org/en-US/docs/Web/API/AudioProcessingEvent)

The `AudioProcessingEvent` represents events that occur when a [`ScriptProcessorNode`](https://developer.mozilla.org/en-US/docs/Web/API/ScriptProcessorNode) input buffer is ready to be processed.

### [Offline/background audio processing](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API\#offlinebackground_audio_processing)

It is possible to process/render an audio graph very quickly in the background — rendering it to an [`AudioBuffer`](https://developer.mozilla.org/en-US/docs/Web/API/AudioBuffer) rather than to the device's speakers — with the following.

[`OfflineAudioContext`](https://developer.mozilla.org/en-US/docs/Web/API/OfflineAudioContext)

The **`OfflineAudioContext`** interface is an [`AudioContext`](https://developer.mozilla.org/en-US/docs/Web/API/AudioContext) interface representing an audio-processing graph built from linked together [`AudioNode`](https://developer.mozilla.org/en-US/docs/Web/API/AudioNode) s. In contrast with a standard `AudioContext`, an `OfflineAudioContext` doesn't really render the audio but rather generates it, _as fast as it can_, in a buffer.

[`complete`](https://developer.mozilla.org/en-US/docs/Web/API/OfflineAudioContext/complete_event "complete") (event)

The `complete` event is fired when the rendering of an [`OfflineAudioContext`](https://developer.mozilla.org/en-US/docs/Web/API/OfflineAudioContext) is terminated.

[`OfflineAudioCompletionEvent`](https://developer.mozilla.org/en-US/docs/Web/API/OfflineAudioCompletionEvent)

The `OfflineAudioCompletionEvent` represents events that occur when the processing of an [`OfflineAudioContext`](https://developer.mozilla.org/en-US/docs/Web/API/OfflineAudioContext) is terminated. The [`complete`](https://developer.mozilla.org/en-US/docs/Web/API/OfflineAudioContext/complete_event "complete") event uses this interface.

## [Guides and tutorials](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API\#guides_and_tutorials)

[Advanced techniques: Creating and sequencing audio](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Advanced_techniques)

In this tutorial, we're going to cover sound creation and modification, as well as timing and scheduling. We will introduce sample loading, envelopes, filters, wavetables, and frequency modulation. If you're familiar with these terms and looking for an introduction to their application with the Web Audio API, you've come to the right place.

[Background audio processing using AudioWorklet](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Using_AudioWorklet)

This article explains how to create an audio worklet processor and use it in a Web Audio application.

[Basic concepts behind Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Basic_concepts_behind_Web_Audio_API)

This article explains some of the audio theory behind how the features of the Web Audio API work to help you make informed decisions while designing how your app routes audio. If you are not already a sound engineer, it will give you enough background to understand why the Web Audio API works as it does.

[Controlling multiple parameters with ConstantSourceNode](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Controlling_multiple_parameters_with_ConstantSourceNode)

This article demonstrates how to use a `ConstantSourceNode` to link multiple parameters together so they share the same value, which can be changed by setting the value of the `ConstantSourceNode.offset` parameter.

[Example and tutorial: Simple synth keyboard](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Simple_synth)

This article presents the code and working demo of a video keyboard you can play using the mouse. The keyboard allows you to switch among the standard waveforms as well as one custom waveform, and you can control the main gain using a volume slider beneath the keyboard. This example makes use of the following Web API interfaces: `AudioContext`, `OscillatorNode`, `PeriodicWave`, and `GainNode`.

[Using IIR filters](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Using_IIR_filters)

The **`IIRFilterNode`** interface of the [Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API) is an `AudioNode` processor that implements a general [infinite impulse response](https://en.wikipedia.org/wiki/Infinite_impulse_response "External link (opens in new tab)") (IIR) filter; this type of filter can be used to implement tone control devices and graphic equalizers, and the filter response parameters can be specified, so that it can be tuned as needed. This article looks at how to implement one, and use it in a simple example.

[Using the Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)

Let's take a look at getting started with the [Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API). We'll briefly look at some concepts, then study a simple boombox example that allows us to load an audio track, play and pause it, and change its volume and stereo panning.

[Visualizations with Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Visualizations_with_Web_Audio_API)

One of the most interesting features of the Web Audio API is the ability to extract frequency, waveform, and other data from your audio source, which can then be used to create visualizations. This article explains how, and provides a couple of basic use cases.

[Web Audio API best practices](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Best_practices)

There's no strict right or wrong way when writing creative code. As long as you consider security, performance, and accessibility, you can adapt to your own style. In this article, we'll share a number of _best practices_ — guidelines, tips, and tricks for working with the Web Audio API.

[Web audio spatialization basics](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Web_audio_spatialization_basics)

As if its extensive variety of sound processing (and other) options wasn't enough, the Web Audio API also includes facilities to allow you to emulate the difference in sound as a listener moves around a sound source, for example panning as you move around a sound source inside a 3D game.
The official term for this is **spatialization**, and this article will cover the basics of how to implement such a system.

## [Examples](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API\#examples)

You can find a number of examples at our [webaudio-examples repo](https://github.com/mdn/webaudio-examples/ "External link (opens in new tab)") on GitHub.

## [Specifications](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API\#specifications)

| Specification |
| --- |
| [Web Audio API\<br>\# AudioContext](https://webaudio.github.io/web-audio-api/#AudioContext) |

## [Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API\#browser_compatibility)

[Report problems with this compatibility data](https://github.com/mdn/browser-compat-data/issues/new?mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_Audio_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EMDN+page+report+details%3C%2Fsummary%3E%0A%0A*+Query%3A+%60api.AudioContext%60%0A*+Report+started%3A+2026-11-10T23%3A43%3A00.817Z%0A%0A%3C%2Fdetails%3E&title=api.AudioContext+-+%3CSUMMARIZE+THE+PROBLEM%3E&template=data-problem.yml "Report an issue with this compatibility data") •
[View data on GitHub](https://github.com/mdn/browser-compat-data/tree/main/api/AudioContext.json "File: api/AudioContext.json")

Settings

Select the browsers to show in compatibility tables. Your selection is saved in this browser.


### Desktop

Chrome Edge Firefox Safari

Internet Explorer Opera

### Mobile

Chrome Android Firefox for Android Safari on iOS

WebView Android WebView on iOS

Opera Android Samsung Browser

### Server

Bun Deno Node.js

### XR

Quest Browser

### Legend

Browser not available for current feature. No support data available.

|  | desktop | mobile |
| --- | --- | --- |
|  | Chrome | Edge | Firefox | Opera | Safari | Chrome Android | Firefox for Android | Opera Android | Safari on iOS | Samsung Browser | WebView Android | WebView on iOS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `AudioContext` | Chrome – Full support<br>Chrome35<br>more | Edge – Full support<br>Edge12 | Firefox – Full support<br>Firefox25 | Opera – Full support<br>Opera22<br>more | Safari – Full support<br>Safari14.1<br>more | Chrome Android – Full support<br>Chrome Android35<br>more | Firefox for Android – Full support<br>Firefox for Android25 | Opera Android – Full support<br>Opera Android22<br>more | Safari on iOS – Full support<br>Safari on iOS14.5<br>more | Samsung Browser – Full support<br>Samsung Browser3<br>more | WebView Android – Full support<br>WebView Android37<br>more | WebView on iOS – Full support<br>WebView on iOS14.5<br>more |
| [`AudioContext()` constructor](https://developer.mozilla.org/en-US/docs/Web/API/AudioContext/AudioContext) | Chrome – Full support<br>Chrome35<br>footnotemore | Edge – Full support<br>Edge12 | Firefox – Full support<br>Firefox25 | Opera – Full support<br>Opera22<br>footnotemore | Safari – Full support<br>Safari14.1<br>footnotemore | Chrome Android – Full support<br>Chrome Android35<br>footnotemore | Firefox for Android – Full support<br>Firefox for Android25 | Opera Android – Full support<br>Opera Android22<br>footnotemore | Safari on iOS – Full support<br>Safari on iOS14.5<br>footnotemore | Samsung Browser – Full support<br>Samsung Browser3<br>footnotemore | WebView Android – Full support<br>WebView Android37<br>footnotemore | WebView on iOS – Full support<br>WebView on iOS14.5<br>footnotemore |
| `options.latencyHint` parameter | Chrome – Full support<br>Chrome58 | Edge – Full support<br>Edge79 | Firefox – No support<br>FirefoxNo | Opera – Full support<br>Opera45 | Safari – Full support<br>Safari14.1 | Chrome Android – Full support<br>Chrome Android58 | Firefox for Android – No support<br>Firefox for AndroidNo | Opera Android – Full support<br>Opera Android43 | Safari on iOS – Full support<br>Safari on iOS14.5 | Samsung Browser – Full support<br>Samsung Browser7 | WebView Android – Full support<br>WebView Android58 | WebView on iOS – Full support<br>WebView on iOS14.5 |
| `options.renderSizeHint` parameter<br>Experimental | Chrome – Full support<br>Chrome153 | Edge – Full support<br>Edge153 | Firefox – No support<br>FirefoxNo | Opera – Full support<br>Opera137 | Safari – No support<br>SafariNo | Chrome Android – Full support<br>Chrome Android153 | Firefox for Android – No support<br>Firefox for AndroidNo | Opera Android – Full support<br>Opera Android103 | Safari on iOS – No support<br>Safari on iOSNo | Samsung Browser – No support<br>Samsung BrowserNo | WebView Android – Full support<br>WebView Android153 | WebView on iOS – No support<br>WebView on iOSNo |
| `options.sampleRate` parameter | Chrome – Full support<br>Chrome74 | Edge – Full support<br>Edge79 | Firefox – Full support<br>Firefox61 | Opera – Full support<br>Opera62 | Safari – Full support<br>Safari14.1 | Chrome Android – Full support<br>Chrome Android74 | Firefox for Android – Full support<br>Firefox for Android61 | Opera Android – Full support<br>Opera Android53 | Safari on iOS – Full support<br>Safari on iOS14.5 | Samsung Browser – Full support<br>Samsung Browser11 | WebView Android – Full support<br>WebView Android74 | WebView on iOS – Full support<br>WebView on iOS14.5 |
| `options.sinkId` parameter<br>Experimental | Chrome – Full support<br>Chrome110 | Edge – Full support<br>Edge110 | Firefox – No support<br>FirefoxNo | Opera – Full support<br>Opera96 | Safari – No support<br>SafariNo | Chrome Android – Full support<br>Chrome Android110 | Firefox for Android – No support<br>Firefox for AndroidNo | Opera Android – Full support<br>Opera Android74 | Safari on iOS – No support<br>Safari on iOSNo | Samsung Browser – Full support<br>Samsung Browser21 | WebView Android – Full support<br>WebView Android110 | WebView on iOS – No support<br>WebView on iOSNo |
| [`baseLatency`](https://developer.mozilla.org/en-US/docs/Web/API/AudioContext/baseLatency) | Chrome – Full support<br>Chrome58 | Edge – Full support<br>Edge79 | Firefox – Full support<br>Firefox70 | Opera – Full support<br>Opera45 | Safari – Full support<br>Safari14.1 | Chrome Android – Full support<br>Chrome Android58 | Firefox for Android – Full support<br>Firefox for Android79 | Opera Android – Full support<br>Opera Android43 | Safari on iOS – Full support<br>Safari on iOS14.5 | Samsung Browser – Full support<br>Samsung Browser7 | WebView Android – Full support<br>WebView Android58 | WebView on iOS – Full support<br>WebView on iOS14.5 |
| [`close`](https://developer.mozilla.org/en-US/docs/Web/API/AudioContext/close) | Chrome – Full support<br>Chrome42 | Edge – Full support<br>Edge14 | Firefox – Full support<br>Firefox40 | Opera – Full support<br>Opera29 | Safari – Full support<br>Safari9 | Chrome Android – Full support<br>Chrome Android42 | Firefox for Android – Full support<br>Firefox for Android40 | Opera Android – Full support<br>Opera Android29 | Safari on iOS – Full support<br>Safari on iOS9 | Samsung Browser – Full support<br>Samsung Browser4 | WebView Android – Full support<br>WebView Android42 | WebView on iOS – Full support<br>WebView on iOS9 |
| [`createMediaElementSource`](https://developer.mozilla.org/en-US/docs/Web/API/AudioContext/createMediaElementSource) | Chrome – Full support<br>Chrome15 | Edge – Full support<br>Edge12 | Firefox – Full support<br>Firefox25<br>footnote | Opera – Full support<br>Opera15 | Safari – Full support<br>Safari6 | Chrome Android – Full support<br>Chrome Android18 | Firefox for Android – Full support<br>Firefox for Android25<br>footnote | Opera Android – Full support<br>Opera Android14 | Safari on iOS – Full support<br>Safari on iOS6 | Samsung Browser – Full support<br>Samsung Browser1 | WebView Android – Full support<br>WebView Android4.4 | WebView on iOS – Full support<br>WebView on iOS6 |
| [`createMediaStreamDestination`](https://developer.mozilla.org/en-US/docs/Web/API/AudioContext/createMediaStreamDestination) | Chrome – Full support<br>Chrome25 | Edge – Full support<br>Edge79 | Firefox – Full support<br>Firefox25 | Opera – Full support<br>Opera15 | Safari – Full support<br>Safari11 | Chrome Android – Full support<br>Chrome Android25 | Firefox for Android – Full support<br>Firefox for Android25 | Opera Android – Full support<br>Opera Android14 | Safari on iOS – Full support<br>Safari on iOS11 | Samsung Browser – Full support<br>Samsung Browser1.5 | WebView Android – Full support<br>WebView Android4.4 | WebView on iOS – Full support<br>WebView on iOS11 |
| [`createMediaStreamSource`](https://developer.mozilla.org/en-US/docs/Web/API/AudioContext/createMediaStreamSource) | Chrome – Full support<br>Chrome22 | Edge – Full support<br>Edge12 | Firefox – Full support<br>Firefox25 | Opera – Full support<br>Opera15 | Safari – Full support<br>Safari11 | Chrome Android – Full support<br>Chrome Android25 | Firefox for Android – Full support<br>Firefox for Android25 | Opera Android – Full support<br>Opera Android14 | Safari on iOS – Full support<br>Safari on iOS11 | Samsung Browser – Full support<br>Samsung Browser1.5 | WebView Android – Full support<br>WebView Android4.4 | WebView on iOS – Full support<br>WebView on iOS11 |
| [`createMediaStreamTrackSource`](https://developer.mozilla.org/en-US/docs/Web/API/AudioContext/createMediaStreamTrackSource) | Chrome – No support<br>ChromeNo<br> <br>footnote | Edge – No support<br>EdgeNo<br> <br>footnote | Firefox – Full support<br>Firefox68<br>footnote | Opera – No support<br>OperaNo<br> <br>footnote | Safari – No support<br>SafariNo | Chrome Android – No support<br>Chrome AndroidNo<br> <br>footnote | Firefox for Android – Full support<br>Firefox for Android68<br>footnote | Opera Android – No support<br>Opera AndroidNo<br> <br>footnote | Safari on iOS – No support<br>Safari on iOSNo | Samsung Browser – No support<br>Samsung BrowserNo<br> <br>footnote | WebView Android – No support<br>WebView AndroidNo<br> <br>footnote | WebView on iOS – No support<br>WebView on iOSNo |
| `error` event<br>Experimental | Chrome – Full support<br>Chrome128 | Edge – Full support<br>Edge128 | Firefox – No support<br>FirefoxNo | Opera – Full support<br>Opera114 | Safari – No support<br>SafariNo | Chrome Android – Full support<br>Chrome Android128 | Firefox for Android – No support<br>Firefox for AndroidNo | Opera Android – Full support<br>Opera Android85 | Safari on iOS – No support<br>Safari on iOSNo | Samsung Browser – Full support<br>Samsung Browser28 | WebView Android – Full support<br>WebView Android128 | WebView on iOS – No support<br>WebView on iOSNo |
| [`getOutputTimestamp`](https://developer.mozilla.org/en-US/docs/Web/API/AudioContext/getOutputTimestamp) | Chrome – Full support<br>Chrome57 | Edge – Full support<br>Edge79 | Firefox – Full support<br>Firefox70 | Opera – Full support<br>Opera44 | Safari – Full support<br>Safari14.1 | Chrome Android – Full support<br>Chrome Android57 | Firefox for Android – Full support<br>Firefox for Android79 | Opera Android – Full support<br>Opera Android43 | Safari on iOS – Full support<br>Safari on iOS14.5 | Samsung Browser – Full support<br>Samsung Browser7 | WebView Android – Full support<br>WebView Android57 | WebView on iOS – Full support<br>WebView on iOS14.5 |
| [`outputLatency`](https://developer.mozilla.org/en-US/docs/Web/API/AudioContext/outputLatency) | Chrome – Full support<br>Chrome102 | Edge – Full support<br>Edge102 | Firefox – Full support<br>Firefox70 | Opera – Full support<br>Opera88 | Safari – Full support<br>Safari18.4 | Chrome Android – Full support<br>Chrome Android102 | Firefox for Android – Full support<br>Firefox for Android79 | Opera Android – Full support<br>Opera Android70 | Safari on iOS – Full support<br>Safari on iOS18.4 | Samsung Browser – Full support<br>Samsung Browser19 | WebView Android – Full support<br>WebView Android102 | WebView on iOS – Full support<br>WebView on iOS18.4 |
| [`playbackStats`\<br>Experimental](https://developer.mozilla.org/en-US/docs/Web/API/AudioContext/playbackStats) | Chrome – Full support<br>Chrome146 | Edge – Full support<br>Edge146 | Firefox – No support<br>FirefoxNo | Opera – Full support<br>Opera130 | Safari – No support<br>SafariNo | Chrome Android – Full support<br>Chrome Android146 | Firefox for Android – No support<br>Firefox for AndroidNo | Opera Android – Full support<br>Opera Android97 | Safari on iOS – No support<br>Safari on iOSNo | Samsung Browser – No support<br>Samsung BrowserNo | WebView Android – Full support<br>WebView Android146 | WebView on iOS – No support<br>WebView on iOSNo |
| [`resume`](https://developer.mozilla.org/en-US/docs/Web/API/AudioContext/resume) | Chrome – Full support<br>Chrome41 | Edge – Full support<br>Edge14 | Firefox – Full support<br>Firefox40 | Opera – Full support<br>Opera28 | Safari – Full support<br>Safari9 | Chrome Android – Full support<br>Chrome Android41 | Firefox for Android – Full support<br>Firefox for Android40 | Opera Android – Full support<br>Opera Android28 | Safari on iOS – Full support<br>Safari on iOS9 | Samsung Browser – Full support<br>Samsung Browser4 | WebView Android – Full support<br>WebView Android41 | WebView on iOS – Full support<br>WebView on iOS9 |
| [`setSinkId`\<br>Experimental](https://developer.mozilla.org/en-US/docs/Web/API/AudioContext/setSinkId) | Chrome – Full support<br>Chrome110 | Edge – Full support<br>Edge110 | Firefox – No support<br>FirefoxNo | Opera – Full support<br>Opera96 | Safari – No support<br>SafariNo | Chrome Android – Full support<br>Chrome Android110 | Firefox for Android – No support<br>Firefox for AndroidNo | Opera Android – Full support<br>Opera Android74 | Safari on iOS – No support<br>Safari on iOSNo | Samsung Browser – Full support<br>Samsung Browser21 | WebView Android – Full support<br>WebView Android110 | WebView on iOS – No support<br>WebView on iOSNo |
| [`sinkId`\<br>Experimental](https://developer.mozilla.org/en-US/docs/Web/API/AudioContext/sinkId) | Chrome – Full support<br>Chrome110 | Edge – Full support<br>Edge110 | Firefox – No support<br>FirefoxNo | Opera – Full support<br>Opera96 | Safari – No support<br>SafariNo | Chrome Android – Full support<br>Chrome Android110 | Firefox for Android – No support<br>Firefox for AndroidNo | Opera Android – Full support<br>Opera Android74 | Safari on iOS – No support<br>Safari on iOSNo | Samsung Browser – Full support<br>Samsung Browser21 | WebView Android – Full support<br>WebView Android110 | WebView on iOS – No support<br>WebView on iOSNo |
| [`sinkchange` event\<br>Experimental](https://developer.mozilla.org/en-US/docs/Web/API/AudioContext/sinkchange_event) | Chrome – Full support<br>Chrome110 | Edge – Full support<br>Edge110 | Firefox – No support<br>FirefoxNo | Opera – Full support<br>Opera96 | Safari – No support<br>SafariNo | Chrome Android – Full support<br>Chrome Android110 | Firefox for Android – No support<br>Firefox for AndroidNo | Opera Android – Full support<br>Opera Android74 | Safari on iOS – No support<br>Safari on iOSNo | Samsung Browser – Full support<br>Samsung Browser21 | WebView Android – Full support<br>WebView Android110 | WebView on iOS – No support<br>WebView on iOSNo |
| [`suspend`](https://developer.mozilla.org/en-US/docs/Web/API/AudioContext/suspend) | Chrome – Full support<br>Chrome41 | Edge – Full support<br>Edge14 | Firefox – Full support<br>Firefox40 | Opera – Full support<br>Opera28 | Safari – Full support<br>Safari9 | Chrome Android – Full support<br>Chrome Android41 | Firefox for Android – Full support<br>Firefox for Android40 | Opera Android – Full support<br>Opera Android28 | Safari on iOS – Full support<br>Safari on iOS9 | Samsung Browser – Full support<br>Samsung Browser4 | WebView Android – Full support<br>WebView Android41 | WebView on iOS – Full support<br>WebView on iOS9 |

### Legend

Tip: you can click/tap on a cell for more information.


Full supportFull support

No supportNo support

Experimental. Expect behavior to change in the future.

See implementation notes.

Requires a vendor prefix or different name for use.

Has more compatibility info.

## [See also](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API\#see_also)

### [Tutorials/guides](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API\#tutorialsguides)

- [Basic concepts behind Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Basic_concepts_behind_Web_Audio_API)
- [Using the Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)
- [Advanced techniques: creating sound, sequencing, timing, scheduling](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Advanced_techniques)
- [Autoplay guide for media and Web Audio APIs](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Autoplay)
- [Using IIR filters](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Using_IIR_filters)
- [Visualizations with Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Visualizations_with_Web_Audio_API)
- [Web audio spatialization basics](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Web_audio_spatialization_basics)
- [Controlling multiple parameters with ConstantSourceNode](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Controlling_multiple_parameters_with_ConstantSourceNode)
- [Mixing Positional Audio and WebGL (2012)](https://web.dev/articles/webaudio-positional-audio "External link (opens in new tab)")
- [Developing Game Audio with the Web Audio API (2012)](https://web.dev/articles/webaudio-games "External link (opens in new tab)")

### [Libraries](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API\#libraries)

- [Tone.js](https://tonejs.github.io/ "External link (opens in new tab)"): a framework for creating interactive music in the browser.
- [howler.js](https://github.com/goldfire/howler.js/ "External link (opens in new tab)"): a JS audio library that defaults to [Web Audio API](https://webaudio.github.io/web-audio-api/ "External link (opens in new tab)") and falls back to [HTML Audio](https://html.spec.whatwg.org/multipage/media.html#the-audio-element "External link (opens in new tab)"), as well as providing other useful features.
- [Mooog](https://github.com/mattlima/mooog "External link (opens in new tab)"): jQuery-style chaining of AudioNodes, mixer-style sends/returns, and more.
- [XSound](https://xsound.jp/ "External link (opens in new tab)"): Web Audio API Library for Synthesizer, Effects, Visualization, Recording, etc.
- [OpenLang](https://github.com/chrisjohndigital/OpenLang "External link (opens in new tab)"): HTML video language lab web application using the Web Audio API to record and combine video and audio from different sources into a single file ( [source on GitHub](https://github.com/chrisjohndigital/OpenLang "External link (opens in new tab)"))
- [Pts.js](https://ptsjs.org/ "External link (opens in new tab)"): Simplifies web audio visualization ( [guide](https://ptsjs.org/guide/sound-0800 "External link (opens in new tab)"))

### [Related topics](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API\#related_topics)

- [Web media technologies](https://developer.mozilla.org/en-US/docs/Web/Media)
- [Guide to media types and formats on the web](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats)

## Help improve MDN

Was this page helpful to you?

YesNo

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/contributors.txt).


[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/web_audio_api/index.md?plain=1 "Folder: en-us/web/api/web_audio_api (Opens in a new tab)") • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_Audio_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fweb_audio_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_Audio_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fweb_audio_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3143a6094e7b87cf1a96b61f9551fb4d95049777%0A*+Document+last+modified%3A+2026-08-27T07%3A36%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
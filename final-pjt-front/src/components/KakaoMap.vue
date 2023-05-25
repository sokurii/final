<template>
  <div>
    <div id="map">
    </div>
    <div id="menu_wrap" class="bg_white">
      <ul id="placesList"></ul>
      <div id="pagination"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'KakaoMap',
  data() {
    return {
        map: null,
        KAKAO_API_KEY: process.env.VUE_APP_KAKAO_API_KEY,
        markers: [],
    }
  },
  props: {
    datas: Object,
  },
  mounted() {
    if (window.kakao && window.kakao.maps) {
        this.loadMap()
    } else {
        this.loadScript()
    }
  },
  methods: {
    // api 불러오기
    loadScript() {
        const script = document.createElement("script")
        script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${this.KAKAO_API_KEY}&autoload=false`
        script.onload = () => window.kakao.maps.load(this.loadMap)

        document.head.appendChild(script)
    },
    // 지도 출력
    loadMap () {
        const container = document.getElementById("map")
        const options = {
            center: new window.kakao.maps.LatLng(35.096378878315, 128.85365157034527), // (위도, 경도)
            level: 2
            // 초기 위치는 SSAFY 부울경 캠퍼스
        }

        this.map = new window.kakao.maps.Map(container, options)
        this.loadMarker()
    },
    // 마커 생성
    loadMarker() {
        // SSAFY 부울경 캠퍼스에 마커 생성
        const markerPosition = new window.kakao.maps.LatLng(
            35.096378878315,
            128.85365157034527
        )
        const marker = new window.kakao.maps.Marker({
            position: markerPosition,
        })
        marker.setMap(this.map)
    }
  }
}
</script>


<style scoped>
#map {
  margin: 3px;
  display: flex;
  border: solid;
  height: 500px;
}
</style>